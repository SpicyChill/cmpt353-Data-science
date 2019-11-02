#!/usr/bin/env python
# coding: utf-8

# In[1]:


from xml.dom import minidom
import sys
import pandas as pd
import numpy as np
from math import sqrt,asin,cos,pi
from pykalman import KalmanFilter


# In[2]:


def latt(x):
        return x.getAttribute('lat')
def lonn(x):
        return x.getAttribute('lon')
def get_data(file):
    d = minidom.parse(file)
    data = d.getElementsByTagName('trkpt')
    get_latitude = np.vectorize(latt,otypes=[np.float])
    get_lontitude = np.vectorize(lonn,otypes=[np.float])
    data_frame = pd.DataFrame()
    data_frame['lat']=get_latitude(data)
    data_frame['lon']=get_lontitude(data)
    return data_frame


# In[3]:


def dist(latitude2,latitude,lontitude2,lontitude):
    p = pi/180
    lat2 = latitude2
    lat = latitude
    lon2 = lontitude2
    lon = lontitude
    a = 0.5 - cos((lat2-lat)*p)/2 + cos(lat*p) * cos(lat2*p) * (1- cos((lon2-lon)*p))/2
    return 12742*asin(sqrt(a))
def distance(data):
    data2= data.copy()
    data2 = data2.shift(periods=1,fill_value=None)
    data2['lon2']=data['lon']
    data2['lat2']=data['lat']
    get_dis = np.vectorize(dist,otypes=[np.float])
    data2['distance']=get_dis(data2['lat2'],data2['lat'],data2['lon2'],data2['lon'])
    new_data = data2['distance']
    total_distance = new_data.sum()
    return total_distance*1000


# In[ ]:





# In[4]:


def smooth(data_e):
    initial_state = data_e.iloc[0]
    observation_covariance = np.diag([15/1000,15/1000]) ** 2
    transition_covariance = np.diag([10/1000,10/1000])**2
    transition = np.identity(2)
    
    kf = KalmanFilter(initial_state_mean = initial_state,
                  initial_state_covariance = observation_covariance,
                  observation_covariance = observation_covariance, 
                  transition_covariance = transition_covariance, 
                  transition_matrices = transition)
    new_data, _=kf.smooth(data_e)
    new_data = pd.DataFrame(data=new_data, columns=data_e.columns)
    return new_data


# In[5]:


def output_gpx(points, output_filename):
    """
    Output a GPX file with latitude and longitude from the points DataFrame.
    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)
    
    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)
    
    points.apply(append_trkpt, axis=1, trkseg=trkseg, doc=doc)
    
    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')


def main():
    #file = 'walk1.gpx'
    file = sys.argv[1]
    points = get_data(file)
   
    print('Unfiltered distance: %0.2f' % (distance(points),))
    
    smoothed_points = smooth(points)
    print('Filtered distance: %0.2f' % (distance(smoothed_points),))
    output_gpx(smoothed_points, 'out.gpx')


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




