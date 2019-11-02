#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys
from math import pi
import matplotlib.pyplot as plt


# In[2]:


stations_file = sys.argv[1]
city_info_file = sys.argv[2]
filename3 = sys.argv[3]


# In[3]:


#stations_file = 'stations.json.gz'
#city_info_file = 'city_data.csv'
#filename3 = 'output.svg'


# In[4]:


stations_info = pd.read_json(stations_file, lines=True)
stations_info['avg_tmax'] = stations_info['avg_tmax'].apply(lambda x:x/10)


# In[5]:


city_info = pd.read_csv(city_info_file)
city_info['area']=city_info['area'].apply(lambda x:x/1e+6)
city_info.dropna(inplace = True)
city_info = city_info[city_info['area'] <= 1000]
city_info['density'] = city_info['population']/city_info['area']



# In[6]:


def distance(city, stations):
    p = pi/180
    city_lat = city['latitude']
    city_long = city['longitude']
    d = 0.5 - np.cos((stations_info['latitude']-city_lat)*p)/2 + np.cos(city_lat*p) * np.cos(stations_info['latitude']*p) * (1- np.cos((stations_info['longitude']-city_long)*p))/2
    return 12742*np.arcsin(np.sqrt(d))


# In[7]:


def best_tmax(city, stations): 
    stations_info['distance'] = distance(city, stations)
    station = stations_info[stations['distance'] == stations_info['distance'].min()]
    station = station.reset_index(drop=True)
    
    return station.loc[0, 'avg_tmax']
    


# In[8]:


city_info['avg_tmax']=city_info.apply(best_tmax, axis=1, stations=stations_info)


# In[9]:


plt.scatter(city_info['avg_tmax'], city_info['density'])
plt.title('Temperature vs Population Density')
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.ylabel('Population Density (people/km\u00b2)')


# In[10]:


#plt.show()
plt.savefig(output_file)

