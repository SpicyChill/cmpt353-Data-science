#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


filename1 = sys.argv[1]
filename2 = sys.argv[2]


# In[3]:


#filename1 = 'pagecounts-20190509-120000.txt'
#filename2 = 'pagecounts-20190509-130000.txt'
data1=pd.read_csv(filename1, sep=' ', header=None, index_col=1,names=['lang', 'page', 'views', 'bytes'])


# In[4]:


data2=pd.read_csv(filename2, sep=' ', header=None, index_col=1,names=['lang', 'page', 'views', 'bytes'])


# In[5]:


data = data1.sort_values(by='views',ascending=False)
new_Data_frame = data1[['views']].copy()
new_Data_frame['views2'] = data2[['views']]


# In[6]:


plt.figure(figsize=(13, 6)) # change the size to something sensible
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.plot(data['views'].values)
plt.title(' Distribution of Views')
plt.ylabel('Views')
plt.xlabel('pages')

plt.subplot(1, 2, 2) # ... and then select the second
plt.xscale('log')
plt.yscale('log')
plt.plot(new_Data_frame['views'],new_Data_frame['views2'], 'b.')
plt.title('Daily Views')
plt.ylabel('data2')
plt.xlabel('data1')
#plt.show()
plt.savefig('wikipedia.png')


# In[ ]:





# In[ ]:





# In[ ]:




