#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']


# In[3]:


print("Row with lowest total precipitation:")


# In[4]:


print(np.sum(totals,axis=1).argmin())


# In[5]:


print("Average precipitation in each month:")


# In[10]:


arr=np.sum(totals,axis=0)
print(np.divide(arr,np.sum(counts,axis= 0)))


# In[11]:


print("Average precipitation in each city:")


# In[12]:


arr2=np.sum(totals,axis=1)
print(np.divide(arr2,np.sum(counts,axis= 1)))


# In[14]:


print("Quarterly precipitation totals:")


# In[16]:


print(np.reshape(totals,(-1,4,3)).sum(axis=2))

