
import re
import nltk
from nltk.corpus import stopwords
import requests
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

def Transform(inputString, lower = True):
    """
    Removes puctuation marks, lowers and splits the string into words and removes stop words from the list
    """
    # remove punctuation marks from string
    string = re.sub("[^a-zA-Z0-9]", " ", inputString)
    
    if(lower):
        string = string.lower()
    
    #split the string
    words = string.split()
    
    #remove stop words
    stopwrds = set(stopwords.words("english"))
    noSW = [w for w in words if w not in stopwrds]
    
    return noSW

#synWord =[['find a lost item', 'find', 'find inform', 'rout up', 'explore', 'forag', 'frisk', 'hunt', 'look', 'manhunt', 'pursuit',
# 'quest', 'ransack', 'scour', 'search'],['add', 'comput a sum', 'add on', 'adjoin', 'button', 'butyl', 'compound', 'concaten', 'enrich', 'foot', 'fortifi',
#                                         'gild the lili', 'include', 'inject', 'intercal']]
synWord =[]
# In[47]:



string1 = "look for Himanshu Singh"
string2 = "Can you search for himanshu singh"
string3 = "LinkedIn, add an experience in my profile"
string4 = "find Himans"
string5 = "What even himan?"
# string6 = "I want to see Himan's profile"


# In[48]:

word1 = "search"
#word2 = "add"
word2 = "apply"

wordList = [word1, word2]
#for number in range(1, 6):
words = Transform(string1)

print("Tranformed string is: " + str(words))

flag = 0
for word in words:
    for idx, synonyms in enumerate(synWord): 
        if(word in synonyms):        
            print("Operation: " + wordList[idx])
            flag = 1
            break
        
    if(flag == 1):
        break

if(flag == 0):
    print("You are not speaking a valid operation")
