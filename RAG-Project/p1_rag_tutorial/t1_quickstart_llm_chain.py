import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = 

llm = ChatOpenAI()
print(llm.invoke("你知道langsmith是什么吗?"))
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])
chain = prompt | llm
print(chain.invoke({"input": "你知道langsmith是什么吗?"}))
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
print(chain.invoke({"input": "你知道langsmith是什么吗?"}))
