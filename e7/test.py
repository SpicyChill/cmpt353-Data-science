import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import lab2rgb
import sys
# .reshape((-1,3))
data = pd.read_csv('colour-data.csv')
X = data[['R', 'G', 'B']]/255
X
X = np.array([data['R'],data['G'],data['B']]).transpose().reshape((-1,3))
y = data['Label']
y
y = np.array(data['Label']).transpose()
y