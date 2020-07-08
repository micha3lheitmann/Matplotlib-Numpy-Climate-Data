#!/usr/bin/env python
# coding: utf-8

# In[54]:


import matplotlib as mpl

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=20,10


# In[55]:


data = np.genfromtxt('Matplotlib-Numpy-Climate-Data\Climate_Data.csv', delimiter=',', dtype=None, skip_header=5, names=('date', 'value', 'anomaly'))


# In[56]:


plt.title('Global Land and Ocean Temperature Anomalies, June')
plt.xlabel('year')
plt.ylabel('degrees F +/- from average')
plt.bar(data['date'], data['value'], color='blue')
plt.show()




