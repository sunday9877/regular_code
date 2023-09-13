#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:16:04 2021

@author: sangdi
"""

import os
from glob import glob

directory1 = 'natf'
source_path = "/Users/sangdi/dust/epic/nc/"


date = 20181201
nday = 31

for n in range(0,nday):
    datestr = str(date + n)
    parent_dir = os.path.join(source_path, datestr)
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)    
    orfiles = sorted(glob(source_path + '/*'+datestr+'*.nc'))
    for ifile,file in enumerate(orfiles):
        filename = os.path.basename(file)
        os.rename(source_path + filename, parent_dir + '/' + filename)