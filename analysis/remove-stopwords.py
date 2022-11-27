from stopwordsiso import stopwords
import jieba
import emoji
import unicodedata

stopwords_list = list(stopwords(["zh"]))

original_text = "👍这部片123"
text = jieba.cut(original_text)

punc_list = '[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：；《）《》“”()»〔〕-]+ '
tokens_without_sw = [words for words in text if not words in list(stopwords(["zh"])) and not words in punc_list]

print(tokens_without_sw)

def word_count(words):
  wordcount = 0
  wordcount_CN = 0
  wordcount_EN = 0
  wordcount_N = 0
  start = True
  for word in words:
    cat = unicodedata.category(word)
    if cat == 'Lo':        # Chinese Letter
      wordcount += 1       # each letter counted as a word
      wordcount_CN += 1
      start = True                       
    elif cat[0] == 'P':    # Some kind of punctuation
      # wordcount += 1     
      start = True                       
    elif cat[0] == 'Z':    # Some kind of separator
      start = True
    else:                  # Everything else
      if start:            
        wordcount += 1     # Only count at the start
        if cat[0]== 'N':
            wordcount_N += 1
        else:
            wordcount_EN += 1
      start = False
  return (wordcount_CN, wordcount_EN, wordcount_N, wordcount) 

print("original chinese counting",word_count(original_text)[0])

wordcount_list = [0, 0, 0, 0]
for words in tokens_without_sw:
    #words = unicodedata.normalize('NFD', words)
    wordcount_list = [a + b for a, b in zip(wordcount_list, word_count(words))]
print(wordcount_list)