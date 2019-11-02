#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[13]:


totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])


# In[3]:


print("City with lowest total precipitation:")


# In[6]:


print(np.sum(totals,axis=1).idxmin())


# In[7]:


print("Average precipitation in each month:")


# In[10]:


print(np.divide(np.sum(totals,axis=0),np.sum(counts,axis=0)))


# In[11]:


print("Average precipitation in each city:")


# In[12]:


print(np.divide(np.sum(totals,axis=1),np.sum(counts,axis=1)))


# In[ ]:




