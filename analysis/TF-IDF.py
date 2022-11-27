import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import jieba

texts = [
    ['没想到', '这是', '唯一', '一部', '尊重', '春节', '档', '电影'],
    ['电影院', '没', '开', '空调', '一直', '冻', '我能', '直接', '睡过去']
]

def dummy_fun(doc):
    return doc

tfidf = TfidfVectorizer(
    tokenizer=dummy_fun,
    preprocessor=dummy_fun,
    token_pattern=None,
    use_idf=True) 

X = tfidf.fit_transform(texts)
print(X)

df = pd.DataFrame(X.toarray(), columns=tfidf.get_feature_names())
print(df)