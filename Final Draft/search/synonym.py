
# coding: utf-8

# In[3]:


import re
import nltk
from nltk.corpus import stopwords
import requests
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


# In[15]:


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


# In[7]:




# In[9]:


def findSynonyms(word1, level = 'start'):
    """
    returns a list of the synynoms of the word by considering the level(start or end)
    """
    tofind = "http://api.conceptnet.io/c/en/" + word1
    obj = requests.get(tofind).json()
    
    #copy all the snynonyms in a list
    synWord = []
    
    for i in range(len(obj['edges'])):
        synWord.append(obj['edges'][i][level]['label'])

    return synWord


# In[10]:


# stemming and lemitization


# In[11]:


def stemming(synWord):
    ps = PorterStemmer()

    # Stemming
    StemmedSynWord = []
    for idx, w in enumerate(synWord):
        w = word_tokenize(w)
        tempword = ""
        for index, every in enumerate(w):
            tempword = tempword + (ps.stem(every))
            if (index != len(w) - 1):
                tempword = tempword + " "
        if(tempword not in StemmedSynWord):
            StemmedSynWord.append(tempword)

    return StemmedSynWord


# In[22]:


def lemmitization(StemmedSynWord):
    wl = WordNetLemmatizer()
    
    # lemmatization
    lemmaSynWord = []
    for idx, w in enumerate(StemmedSynWord):
        w = word_tokenize(w)
        tempword = ""
        for index, every in enumerate(w):
            tempword = tempword + (wl.lemmatize(every))
            if (index != len(w) - 1):
                tempword = tempword + " "
        if(tempword not in lemmaSynWord):
            lemmaSynWord.append(tempword)

    return lemmaSynWord


# In[34]:


# words whose synonyms are to be found
word1 = "search"
word2 = "add"

wordList = [word1, word2]

synWord = []
for word in wordList:
    print("Finding synonyms of the word " + word + "...")
    synWord = findSynonyms(word)

    print("Stemming...")
    StemmedSynWord = stemming(synword)

    print("Lemmitizating...")
    lemmaSynWord = lemmitization(StemmedSynWord)

    print("Resultant list: ")
    print(lemmaSynWord)
    
    print("\n")
    synWord.append(lemmaSynWord)


# In[47]:


string1 = "look for himanshu singh"
string2 = "Can you search for himanshu singh"
string3 = "LinkedIn, add an experience in my profile"
string4 = "find Himans"
string5 = "What even himan?"
# string6 = "I want to see Himan's profile"


# In[48]:
