# -*- coding: utf-8 -*-

import unicodedata

s = u" 我們的 nkenfsf , sdfsf"     

def word_count(text):
  wordcount = 0
  wordcount_CN = 0
  wordcount_EN = 0
  start = True
  for c in text:      
    cat = unicodedata.category(c)
    print(cat)
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
        wordcount_EN += 1
      start = False
  return (wordcount_CN, wordcount_EN, wordcount) 


print(word_count(s)[0])