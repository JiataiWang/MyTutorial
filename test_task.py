from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.optim import Adam
import pandas as pd
import torch
data = pd.read_csv("../demo_data/ChnSentiCorp_htl_all.csv")
data = data.dropna()

#创建dataset

class MyDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        self.data = pd.read_csv("./ChnSentiCorp_htl_all.csv")
        self.data = self.data.dropna()
    def __getitem__(self, index):
        return self.data.iloc[index]["review"], self.data.iloc[index]["label"]
    def __len__(self):
        return len(self.data)
dataset = MyDataset()
for i in range(5):
    print(dataset[i])

#划分数据集
from torch.utils.data import random_split
trainset, validset = random_split(dataset, lengths=[0.9, 0.1])
for i in range(10):
    print(trainset[i])

#创建dataloader


tokenizer = AutoTokenizer.from_pretrained("rbt3")

def collate_func(batch):
    texts, labels = [], []
    for item in batch:
        texts.append(item[0])
        labels.append(item[1])
    inputs = tokenizer(texts, max_length=128, padding="max_length", truncation=True, return_tensors="pt")
    inputs["labels"] = torch.tensor(labels)
    return inputs

trainloader = DataLoader(trainset, batch_size=32, shuffle=True, collate_fn=collate_func)
validloader = DataLoader(validset, batch_size=64, shuffle=False, collate_fn=collate_func)
print(next(enumerate(validloader))[1])

#创建模型及优化器
model = AutoModelForSequenceClassification.from_pretrained("./rbt3/")
if torch.cuda.is_available():
    model = model.cuda()
optimizer = Adam(model.parameters(), lr=2e-5)

#训练与验证
def evaluate():
    model.eval()
    acc_num = 0
    with torch.inference_mode():
        for batch in validloader:
            if torch.cuda.is_available():
                batch = {k: v.cuda() for k, v in batch.items()}
            output = model(**batch)
            pred = torch.argmax(output.logits, dim=-1)
            acc_num += (pred.long() == batch["labels"].long()).float().sum()
    return acc_num / len(validset)

def train(epoch=3, log_step=100):
    global_step = 0
    for ep in range(epoch):
        model.train()
        for batch in trainloader:
            if torch.cuda.is_available():
                batch = {k: v.cuda() for k, v in batch.items()}
            optimizer.zero_grad()
            output = model(**batch)
            output.loss.backward()
            optimizer.step()
            if global_step % log_step == 0:
                print(f"ep: {ep}, global_step: {global_step}, loss: {output.loss.item()}")
            global_step += 1
        acc = evaluate()
        print(f"ep: {ep}, acc: {acc}")
#训练
train()
#预测
sen = "我觉得这家酒店不错，饭很好吃！"
id2_label = {0: "差评！", 1: "好评！"}
model.eval()
with torch.inference_mode():
    inputs = tokenizer(sen, return_tensors="pt")
    inputs = {k: v.cuda() for k, v in inputs.items()}
    logits = model(**inputs).logits
    pred = torch.argmax(logits, dim=-1)
    print(f"输入：{sen}\n模型预测结果:{id2_label.get(pred.item())}")
#推理
from transformers import pipeline
model.config.id2label = id2_label
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0)
pipe(sen)
