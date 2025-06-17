import torch
import os
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model, PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer

def process_func(example):
    MAX_LENGTH = 256
    input_ids, attention_mask, labels = [], [], []
    instruction = "\n".join([example["instruction"], example["input"]]).strip()     # query
    instruction = tokenizer.build_chat_input(instruction, history=[], role="user")  # [gMASK]sop<|user|> \n query<|assistant|>
    response = tokenizer("\n" + example["output"], add_special_tokens=False)        # \n response, 缺少eos token
    input_ids = instruction["input_ids"][0].numpy().tolist() + response["input_ids"] + [tokenizer.eos_token_id]
    attention_mask = instruction["attention_mask"][0].numpy().tolist() + response["attention_mask"] + [1]
    labels = [-100] * len(instruction["input_ids"][0].numpy().tolist()) + response["input_ids"] + [tokenizer.eos_token_id]
    if len(input_ids) > MAX_LENGTH:
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

device = torch.device("cuda:3" if torch.cuda.is_available() else "cpu")
ds = Dataset.load_from_disk("/wangjiatai/project/algorithm/huggingface_debug/demo_data/alpaca_data_zh")
tokenizer = AutoTokenizer.from_pretrained("/wangjiatai/weight/chatglm3-6b-base", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/wangjiatai/weight/chatglm3-6b-base", trust_remote_code=True, low_cpu_mem_usage=True, 
                                             torch_dtype=torch.half, device_map="auto", load_in_8bit=True)



tokenized_ds = ds.map(process_func, remove_columns=ds.column_names)
tokenizer.decode(tokenized_ds[1]["input_ids"])
tokenizer.decode(list(filter(lambda x: x != -100, tokenized_ds[1]["labels"])))

#配置微调文件
config = LoraConfig(target_modules=["query_key_value"])
model = get_peft_model(model, config)
model.print_trainable_parameters()

args = TrainingArguments(
    output_dir="/wangjiatai/runs",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=16,
    logging_steps=10,
    num_train_epochs=1,
    learning_rate=1e-4,
    remove_unused_columns=False
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_ds.select(range(6000)),
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
)

trainer.train()
model.eval()
print(model.chat(tokenizer, "数学考试怎么考高分？", history=[])[0])
trainer.model.save_pretrained('/wangjiatai/runs')


pass