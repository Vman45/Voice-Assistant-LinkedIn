
# coding: utf-8

# In[46]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from nltk.stem import PorterStemmer

from LinkedIn_Operation_identification import findSynonyms


# In[56]:


todo = ['position', 'openings', 'profiles', 'jobs']
synonymz = []

for cur in todo:
    synCur = findSynonyms(cur)
    curSyn = [cur]
    for syn in synCur:
        if syn not in curSyn:
            curSyn.append(syn)
    synonymz.append(curSyn)


# In[54]:


# synonymz


# In[57]:


import os
os.environ["CORENLP_HOME"] = '/home/shreya\stanford-corenlp-full-2018-02-27'

from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000/')


# In[58]:


def stemming(text):
    ps = PorterStemmer()

    w = word_tokenize(text)
    tempword = ""
    for index, every in enumerate(w):
        tempword = tempword + (ps.stem(every))
        if (index != len(w) - 1):
            tempword = tempword + " "

    return tempword


# In[59]:


text = ('sales jobs at LinkedIn')
# text = stemming(text)

output = nlp.annotate( text, properties = { 
    'annotators' : 'tokenize, ssplit, pos, depparse, parse',
    'outputFormat': 'json'})


# In[60]:


depTreeStr = output['sentences'][0]['parse']
print(depTreeStr)


# In[61]:


from nltk.tree import ParentedTree
ptree = ParentedTree.fromstring(depTreeStr)
ptree


# In[62]:


leaf_values = ptree.leaves()

tree_location = []
flag = 0

for cur in synonymz:
    for word in cur:
        if word in leaf_values:
            leaf_index = leaf_values.index(word)
            tree_location = ptree.leaf_treeposition(leaf_index)
            print (tree_location)
            print (ptree[tree_location])
            flag = 1
            break
    if(flag == 1):
        break


# In[63]:


treeLoc = tree_location[:-2]
print(treeLoc)

subtree = ptree[treeLoc]
position = ""
if(treeLoc != []):
    childNodes = subtree.leaves()
    print(childNodes)

    position = (" ".join(childNodes))
    print(position)

subtree


# In[64]:


position

