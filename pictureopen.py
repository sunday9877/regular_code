# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:53:58 2019

@author: Sunday
"""
#open picture file
import numpy as np
import matplotlib.pyplot as plt

path ='D:\\image\\process\\'
name = '0613_664A'
NRCS = np.load(path+name+'.npy')
a=np.ma.array(NRCS, mask=np.isnan(NRCS))
plt.imshow(np.where(a>0.01, 0.01, a), cmap='gray') 