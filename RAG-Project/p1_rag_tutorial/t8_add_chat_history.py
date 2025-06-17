import os
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

os.environ["OPENAI_API_KEY"] = 
path = '/Users/titus.w/Code/data/prodata_rag_QC_v1'
text_loader_kwargs = {'autodetect_encoding': True}
loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())


# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
#多轮对话prompt，第一轮和后面几轮用的提示词不同
#第二轮对话以后输入一个元组(history, question)
contextualize_q_system_prompt = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)
#第一轮对话输入一个元组(history, context, question)
first_qa_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", first_qa_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

#第二轮对话之后所用的链
contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()
def contextualized_question(input: dict):
    if input.get("chat_history"):
        return contextualize_q_chain
    else:
        return input["question"]

#每轮都得检索，第一轮的query是什么？第二轮的query是什么？
multi_qa_rag_chain = (
    RunnablePassthrough.assign(
    # if history exists, mianchchain use subchain to rebuild the question
        context=contextualized_question | retriever | format_docs
    )
    | qa_prompt
    | llm
)

go_on = True
chat_history = []
while go_on:
    query_text = input("你的问题: ")
    if 'exit' in query_text:
        break
    ai_msg = multi_qa_rag_chain.invoke({"question": query_text, "chat_history": chat_history})
    chat_history.extend([HumanMessage(content=query_text), ai_msg])
    print(ai_msg)