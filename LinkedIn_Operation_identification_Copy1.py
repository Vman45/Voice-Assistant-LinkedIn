
# coding: utf-8

# In[1]:


import re
import nltk
from nltk.corpus import stopwords

def Transform(inputString, lower = False):
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

import requests

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

# stemming and lemitization
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

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

# words whose synonyms are to be found
word1 = "search"
word2 = "add"

wordList = [word1, word2]

synWord = []
for word in wordList:
    print("Finding synonyms of the word " + word + "...")
    synword = findSynonyms(word)

    print("Stemming...")
    StemmedSynWord = stemming(synword)

    print("Lemmitizating...")
    lemmaSynWord = lemmitization(StemmedSynWord)

    print("Resultant list: ")
    print(lemmaSynWord)
    
    print("\n")
    synWord.append(lemmaSynWord)

string1 = "look for bindu singh"
string2 = "Can you search for himanshu singh"
string3 = "LinkedIn, add an experience in my profile"
string4 = "find Himans"
string5 = "What even himan?"
# string6 = "I want to see Himan's profile"
string7 = "Look for job openings at LinkedIn"
stringr2 = "are there any senior software developer positions at linkedin"

# for number in range(1, 6):
words = Transform(string2)

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

