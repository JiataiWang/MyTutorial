from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig


tokenizer = AutoTokenizer.from_pretrained("/wangjiatai/weight/Baichuan2-13B-Chat",use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/wangjiatai/weight/Baichuan2-13B-Chat", device_map="auto")
model.generation_config = GenerationConfig.from_pretrained("/wangjiatai/weight/Baichuan2-13B-Chat")
app = FastAPI()

# This defines the data json format expected for the endpoint, change as needed
class RequestItem(BaseModel):
    message: str

@app.post("/generate/")
async def generate_text(request_item: RequestItem):
    try:
        # 在这里处理接收到的 JSON 请求
        reqStr = request_item.message
        messages = []
        messages.append({"role": "user", "content": reqStr})
        response = model.chat(tokenizer,messages)
        return {"generated_text": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#uvicorn app:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

