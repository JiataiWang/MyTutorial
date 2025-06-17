#一般的步骤是先分词，然后构造词典映射，然后在根据词典将文本转化为数字，最后填充和截断。
#但是现在都不需要，transformers都封装好了，只需要把数据准备好调用tokenizer就行了
from transformers import AutoTokenizer
sentence = 'I love you.'
tokenizer = AutoTokenizer.from_pretrained('/Users/titus.w/Code/model/Llama-2-7b-chat-hf')
#分词器tokenizer的tokenize方法可以直接分词
tokens = tokenizer.tokenize(sentence)
print(len(tokenizer.vocab))
#词和词索引的相互转化
ids = tokenizer.convert_tokens_to_ids(tokens)
tokens = tokenizer.convert_ids_to_tokens(ids)
ids = tokenizer.encode(sentence, add_special_tokens=True)
#将id序列转化为字符串被称之为解码
str_sen = tokenizer.decode(ids, skip_special_tokens=False)
# 截断
ids = tokenizer.encode(sentence, max_length=2, truncation=True)
# 填充
# ids = tokenizer.encode(sentence, padding="max_length", max_length=15)
attention_mask = [1 if idx != 0 else 0 for idx in ids]
token_type_ids = [0] * len(ids)
#处理batch数据
sens = ["According to Tony Estanguet, president of the Paris Olympics Organizing Committee, a special event with selected athletes in attendance will happen on the River Seine on Wednesday to mark the one-year countdown for the Paris Olympics.",
        "I love you.",
        "Two months out and lagging ticket sales enjoyed a boost from 100-day events and the torch relay."]
res = tokenizer(sens)
#当加载大模型分词器的时候我们添加相信远程代码的参数
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('THUDM/chatglm-6b', trust_remote_code=True)

