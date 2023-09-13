#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:11:30 2021

@author: sangdi
"""


import os
from glob import glob
import datetime
from satpy import Scene
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from satpy.writers import get_enhanced_image
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import tarfile
from satpy import MultiScene
#from pyresample import geometry

import warnings
warnings.filterwarnings("ignore")

###read file
l1bfiles = glob("rawdata/SEVIRI/tar/*.tar")

for ifile,file in enumerate(l1bfiles):
    filename = os.path.basename(file)
 
    # # Directory
directory = filename.split(".")[0]

path_dir = "rawdata/SEVIRI/tar/"
### create new directory
# # Parent Directory path
parent_dir = "rawdata/seviri/"
  
# # Path
path = os.path.join(parent_dir, directory)
os.mkdir(path)


my_tar = tarfile.open(path_dir + filename)
my_tar.extractall(path) # specify which folder to extract to
my_tar.close()

filenames = glob(path + '/*.nc')


mscn = MultiScene.from_files(filenames, reader='seviri_l1b_nc')    
mscn.load(['dust'])
mscn.save_animation('animation/{start_time:%Y%m%d}.mp4', fps=6)
