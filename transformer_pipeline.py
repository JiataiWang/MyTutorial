import torch
import time
import gradio as gr
from transformers.pipelines import SUPPORTED_TASKS,pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
SUPPORTED_TASKS.items()

#先定义一个计时函数
def rockon(pipe):
    times = []
    for i in range(100):
        torch.cuda.synchronize()
        start = time.time()
        pipe("hello")
        torch.cuda.synchronize()
        end = time.time()
        times.append(end - start)
    print(sum(times) / 100)

# 可以直接执行下面代码用于推理
# pipe = pipeline("text-classification")
# 但如果要加载预训练模型，就必须先定义model和tokenizer
model = AutoModelForSequenceClassification.from_pretrained("/root/autodl-tmp/bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/bert-base-uncased")

pipe_cpu = pipeline("text-classification", model=model, tokenizer=tokenizer)
print(pipe_cpu("hello"))
print(pipe_cpu.model.device)
rockon(pipe_cpu)

pipe_gpu = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0)
print(pipe_gpu("hello"))
print(pipe_gpu.model.device)
rockon(pipe_gpu)

#直接启动服务
#gr.Interface.from_pipeline(pipe_gpu).launch(share=True)

input_text = "我觉得不太行！"
inputs = tokenizer(input_text, return_tensors="pt").to('cuda:0')
res = model(**inputs)
logits = res.logits
logits = torch.softmax(logits, dim=-1)
pred = torch.argmax(logits).item()
model.config.id2label
result = model.config.id2label.get(pred)



pass