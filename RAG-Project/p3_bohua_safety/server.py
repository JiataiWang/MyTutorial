from fastapi import FastAPI
from langserve import add_routes
from bohua import multi_qa_rag_chain

app = FastAPI(title='Retrieval App')
add_routes(app,
           multi_qa_rag_chain,
           path="/bh")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8880)
