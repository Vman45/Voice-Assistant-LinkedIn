
# coding: utf-8

# 1. operation identifications => remove
# 2. NER => remove orgnaizations, names, locations
# 3. remove stop words
# 4. tokenize => return

# In[54]:


# operation identification
get_ipython().magic('run "LinkedIn_Operation_identification.ipynb"')

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

def Design(string):
    tokenized = word_tokenize(string)
    # tokenized

    firstRefine = ""
    for word in tokenized:
        flag = 0
        for cur in synWord:
            if(word in cur):
                flag = 1
                break
        if(flag == 0):
            firstRefine += word + " "

    # firstRefine

    tokenized = word_tokenize(firstRefine)

    # NER tagging and removing
    tagged = pos_tag(tokenized)

    # chunking
    ne_chunked_sents = ne_chunk(tagged)

    named_entities = {}
    for tagged_tree in ne_chunked_sents:
      if(hasattr(tagged_tree, 'label')):
          entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
          entity_type = tagged_tree.label() # get NE category
          named_entities[entity_name] = entity_type
#     print(named_entities)

    secondRefine = " ".join([w for w in tokenized if w not in named_entities.keys()])
    # secondRefine

    tokenized = word_tokenize(secondRefine)

    stopwrds = set(stopwords.words("english"))
    thirdRefine = " ". join([w for w in tokenized if w not in stopwrds])

    # thirdRefine

    tokenized = word_tokenize(thirdRefine)
    return tokenized


# In[56]:


string = "search for sales at Amazon"
tokens = Design(string)
tokens

