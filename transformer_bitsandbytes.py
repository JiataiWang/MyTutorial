from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer
import torch
from peft import LoraConfig, TaskType, get_peft_model
def process_func(example):
    MAX_LENGTH = 384    # Llama分词器会将一个中文字切分为多个token，因此需要放开一些最大长度，保证数据的完整性
    input_ids, attention_mask, labels = [], [], []
    instruction = tokenizer("\n".join(["Human: " + example["instruction"], example["input"]]).strip() + "\n\nAssistant: ", add_special_tokens=False)
    response = tokenizer(example["output"] + tokenizer.eos_token, add_special_tokens=False)
    input_ids = instruction["input_ids"] + response["input_ids"]
    attention_mask = instruction["attention_mask"] + response["attention_mask"]
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"]
    if len(input_ids) > MAX_LENGTH:
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

ds = Dataset.load_from_disk("/Users/titus.w/Code/algorithm/huggingface_debug/demo_data/alpaca_data_zh")
print(len("以下是保持健康的三个提示：\n\n1. 保持身体活动。每天做适当的身体运动，如散步、跑步或游泳，能促进心血管健康，增强肌肉力量，并有助于减少体重。"))
tokenizer = AutoTokenizer.from_pretrained("/Users/titus.w/Code/model/Llama-2-7b-chat-hf")
tokenizer.padding_side = "right"  # 一定要设置padding_side为right，否则batch大于1时可能不收敛



tokenized_ds = ds.map(process_func, remove_columns=ds.column_names)
print(tokenizer.decode(tokenized_ds[0]["input_ids"]))
print(tokenizer("呀", add_special_tokens=False)) #词表太小，token表示效率太低
tokenizer.decode(list(filter(lambda x: x != -100, tokenized_ds[1]["labels"])))

model = AutoModelForCausalLM.from_pretrained("/Users/titus.w/Code/model/Llama-2-7b-chat-hf", low_cpu_mem_usage=True, torch_dtype=torch.half, device_map="auto")
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))
for name, parameter in model.named_parameters():
    print(name, parameter.dtype)

config = LoraConfig(task_type=TaskType.CAUSAL_LM,)
model = get_peft_model(model, config)
for name, parameter in model.named_parameters():
    print(name, parameter.dtype)
model.enable_input_require_grads() # 开启梯度检查点时，要执行该方法
model = model.half()  #将lora模型从fp32完全变成半精度训练
for name, parameter in model.named_parameters():
    print(name, parameter.dtype)
model.print_trainable_parameters()
args = TrainingArguments(
    output_dir="./chatbot",
    # per_device_train_batch_size=2,
    # gradient_accumulation_steps=8,
    # logging_steps=10,
    # num_train_epochs=1,
    # gradient_checkpointing=True,
    # adam_epsilon=1e-4  #这个参数
)
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_ds.select(range(6)),
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
)
trainer.train()
model = model.cuda()
ipt = tokenizer("Human: {}\n{}".format("考试有哪些技巧？", "").strip() + "\n\nAssistant: ", return_tensors="pt").to(model.device)
tokenizer.decode(model.generate(**ipt, max_length=128, do_sample=True)[0], skip_special_tokens=True)
torch.tensor(1e-8).half()
trainer.model.save_pretrained('/Users/titus.w/Code/')