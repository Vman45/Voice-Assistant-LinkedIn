# nlp libraries
import re
import nltk
from nltk.corpus import stopwords
import requests
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


sentence = "apply for id 2"
for sent in nltk.sent_tokenize(sentence):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if hasattr(chunk, 'label'):
         print(chunk.label(), ' '.join(c[0] for c in chunk))
      else:
          if(chunk[1]=="CD"):
            print(chunk[0])
