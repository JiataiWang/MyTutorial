import evaluate
evaluate.list_evaluation_modules(include_community=False, with_details=True)
accuracy = evaluate.load("accuracy")
print(accuracy.description)
print(accuracy.inputs_description)
#评估指标计算——全局计算
accuracy = evaluate.load("accuracy")
results = accuracy.compute(references=[0, 1, 2, 0, 1, 2], predictions=[0, 1, 1, 2, 1, 0])
#评估指标计算——迭代计算
accuracy = evaluate.load("accuracy")
for ref, pred in zip([0,1,0,1], [1,0,0,1]):
    accuracy.add(references=ref, predictions=pred)
print(accuracy.compute())
accuracy = evaluate.load("accuracy")
for refs, preds in zip([[0,1],[0,1]], [[1,0],[0,1]]):
    accuracy.add_batch(references=refs, predictions=preds)
accuracy.compute(accuracy.compute())
