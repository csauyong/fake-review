# encoding=utf-8
import jieba
import jieba.posseg as pseg

for token in jieba.cut("我来到北京清华大学"):
    print(token)

tokens = jieba.cut("这部片成本一定很低，那些个特效都算不上五毛，撑死了五分吧，钱肯定是赚的！既扶贫又扶己！赛高！")
print(list(tokens))

'''
from snownlp import SnowNLP

s = SnowNLP(u'这部片成本一定很低，那些个特效都算不上五毛，撑死了五分吧，钱肯定是赚的！既扶贫又扶己！赛高！')

print(s.words)
'''

text = "飞机是今天晚上七点钟准时降落在北京首都国际机场的"
words = pseg.cut(text)
for w in words:
    print('%s %s' % (w.word, w.flag))