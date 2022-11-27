from snownlp import SnowNLP

text = SnowNLP(u'我实在受不了四字弟弟的演技了，我以为少年的你是开始，没想到是巅峰。这种打着骗眼泪的癌症片硬生生拍成了爱情片，我带着孩子都不好意思给孩子看，孩子才七岁很喜欢弟弟，唉')
sent = text.sentences
sent = ["good"]
sum = 0
count = 0
sent_list = []
print(sent)
for sen in sent:
    s = SnowNLP(sen)
    sum += s.sentiments
    count += 1
    sent_list.append(s.sentiments)
print(sum/count)
print(sent_list)
