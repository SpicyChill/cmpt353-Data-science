#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import sys
from difflib import get_close_matches
filename1 = sys.argv[1]
filename2 = sys.argv[2]
filename3 = sys.argv[3]
#filename1 = 'movie_list.txt'
#filename2 = 'movie_ratings.csv'


movie_list = open(filename1).readlines()

movie_rating = pd.read_csv(filename2)


# In[2]:


def search_movie(movie,movie_list):
    match_result = get_close_matches(movie,movie_list)
    if match_result:
        return match_result[0]
    else:
        return None
movie_rating['title']=movie_rating['title'].apply(lambda movie: search_movie(movie,movie_list))


# In[3]:


movie_rating.dropna(inplace=True) #drop row if title is None
result = movie_rating.groupby('title', as_index=False).mean().round(decimals=2)
#get average of movies with same title, 2 decimal places
result.sort_values(by=['title'],ascending=True, inplace=True) #sort by title
result.to_csv(path_or_buf='output.csv',index=False) #

