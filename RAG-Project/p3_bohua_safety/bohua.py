import asyncio
import os
from langchain import hub
from langchain_elasticsearch import ElasticsearchStore
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.embeddings import HuggingFaceEmbeddings,HuggingFaceBgeEmbeddings
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

os.environ["OPENAI_API_KEY"] = 
path = '/Users/titus.w/Code/data/bohua_test'
text_loader_kwargs = {'autodetect_encoding': True}
loader = DirectoryLoader(path, glob="**/*.json", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
docs = loader.load()

#define text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=30,
    length_function=len,
)
doc_list = []
for doc in docs:
    tmp_docs = text_splitter.create_documents([doc.page_content])
    doc_list += tmp_docs

embedding_model = OpenAIEmbeddings()
embedding_dim = len(embedding_model.embed_query('i love you'))
print(f"embedding模型的维度是：{embedding_dim}")

vector_database = ElasticsearchStore(
    es_url='http://localhost:9200',
    index_name='openai',
    embedding=embedding_model,
    es_user='elastic',
    vector_query_field='query_vectors',
    #es_password='<PASSWORD>'
)
# vector_database.add_documents(doc_list)
retriever = vector_database.as_retriever(search_type="similarity", search_kwargs={"k": 6})

#多轮对话prompt，第一轮和后面几轮用的提示词不同
#(history, question) multi_qa_rag_prompt
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

#(history, context, question) qa_frist_round_rag_prompt
multi_qa_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", multi_qa_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

llm = ChatOpenAI( model="gpt-3.5-turbo", max_tokens=1024)

#sub_chain (multi qa)
contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()
def contextualized_question(input: dict):
    if input.get("chat_history"):
        return contextualize_q_chain
    else:
        return input["question"]
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
#<key-value> main_chain
multi_qa_rag_chain = (
    RunnablePassthrough.assign(
    # if history exists, mianchchain use subchain to rebuild the question
        context=contextualized_question | retriever | format_docs
    )
    | qa_prompt
    | llm
)