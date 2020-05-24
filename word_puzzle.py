#!/usr/bin/env python
# coding: utf-8

# In[127]:


import csv
import numpy as np
import sys


# In[126]:


def search(word,line):
    if word in line:
        return("({},{})".format(line.index(word)+1,line.index(word)+len(word)))
    elif word[::-1] in line:
        return("({},{})".format(len(line)-line.index(word[::-1])-1,len(line)-line.index(word[::-1])-len(word)))
file_name=sys.argv[1]#"word_puzzle.csv"
word_name=sys.argv[2]#"word.csv"
word_dict={}
with open(file_name) as f,open(word_name) as w:
    lines=list(csv.reader(f))
    words=list(csv.reader(w))
    words=np.array(words)
    words=list(words.reshape(-1))
    for word in words:
        line_number=1
        for line in lines:
            search_word="".join(line)#joins elements into a single line
            result=search(word,search_word)
            if(result !=None):
                word_dict[word]=[line_number,result]
                break
            line_number+=1
    for key in word_dict:
        words.remove(key)
    lines=list(np.transpose(lines))
    for word in words:
        line_number=1
        for line in lines:
            search_word="".join(line)#joins elements into a single line
            result=search(word,search_word)
            if(result !=None):
                word_dict[word]=[result,line_number]
                break
            line_number+=1
    lines=np.transpose(lines)
for key in word_dict:
    print("{}:{},{}".format(key,word_dict[key][0],word_dict[key][1]))

