from transformers import AutoConfig, AutoModel, AutoTokenizer
model = AutoModel.from_pretrained("/root/autodl-tmp/bert-base-uncased")
print(model.config)
sen = "I love you."
tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/bert-base-uncased")
inputs = tokenizer(sen, return_tensors="pt")
#不带model_head的模型调用
model = AutoModel.from_pretrained("/root/autodl-tmp/bert-base-uncased", output_attentions=True)
output = model(**inputs)
print(output.last_hidden_state.size())
print(len(inputs["input_ids"][0]))
#带model_head的模型调用
from transformers import AutoModelForSequenceClassification, BertForSequenceClassification
clz_model = AutoModelForSequenceClassification.from_pretrained("/root/autodl-tmp/bert-base-uncased", num_labels=10)
clz_model(**inputs)
print(clz_model.config.num_labels)
print(clz_model(**inputs))