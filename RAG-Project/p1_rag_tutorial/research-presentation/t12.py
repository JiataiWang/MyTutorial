
import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_TRACING"] = "false"
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['OPENAI_API_KEY'] = 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
import pandas as pd
from langchain import hub
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# ---------- 2) 读取并清洗 Excel ----------
DATA_DIR = Path("/Users/titus.w/Code/MyProfile/GitHub/RAG-Project/p1_rag_tutorial/research-presentation/")
files = ["data1.xlsx", "data2.xlsx", "data3.xlsx"]

dfs = []
for fn in files:
    xl = pd.ExcelFile(DATA_DIR / fn)
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        df["__source_file__"] = f"{fn}:{sheet}"
        dfs.append(df)

raw_df = pd.concat(dfs, ignore_index=True).dropna(how="all")
raw_df = raw_df.applymap(lambda x: str(x).strip() if pd.notna(x) else x).drop_duplicates()

docs = [
    Document(
        page_content=f"问：{row['问题']}\n答：{row['答案']}",
        metadata={"source": row["__source_file__"], "row": int(idx)},
    )
    for idx, row in raw_df.iterrows()
]

# ---------- 3) 切分 + 嵌入 ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(splits, embedding=embeddings, persist_directory="stategrid_internal_chroma")
retriever = vectordb.as_retriever(search_kwargs={"k": 4})  # 一次取 4 条，提高回答完整度
print("✅ 向量条目：", vectordb._collection.count())

# ---------- 4) Prompt ----------
from langchain.prompts import ChatPromptTemplate
template = """已知以下参考资料，结合你自己的知识，**用中文**回答用户问题。
要求：
- 回答要尽量详细、分条陈述
- 每当使用资料中的信息时，在句子末尾用对应序号引用，如[1]
- 最后新增一行「引用：」按序号列出资料的来源

参考资料：
{context}

问题：{question}
回答："""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    """把检索结果编号，供 LLM 引用"""
    return "\n\n".join(f"[{i+1}] {doc.page_content}" for i, doc in enumerate(docs))

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ---------- 5) 交互式对话 ----------
print("输入问题（exit 退出）：")
while True:
    user_q = input(">>> ").strip()
    if user_q.lower() == "exit":
        break

    answer = rag_chain.invoke(user_q)
    print("\n🤖 回答：\n", answer)

    # 单独打印来源标题 & 片段，方便终端查看
    source_docs = retriever.get_relevant_documents(user_q)
    print("\n🔗 来源摘录：")
    for idx, d in enumerate(source_docs, 1):
        snippet = d.page_content.split("\n")[0][:80]
        print(f"[{idx}] {d.metadata['source']} | {snippet}...")
    print("-" * 70)