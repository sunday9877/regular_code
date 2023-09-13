#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:22:10 2021

@author: sangdi
"""



import os
from glob import glob

directory1 = 'natf'
source_path = "/data/disang/seviri/2018/m05/"


date = 180501
nday = 32

for n in range(0,nday):
    datestr = str(date + n)
    parent_dir = os.path.join(source_path, datestr)
    orfiles = sorted(glob(parent_dir + '*.zip'))
    for ifile,file in enumerate(orfiles):
        filename = os.path.basename(file)
        if os.path.exists(parent_dir + filename):
            os.remove(parent_dir + filename)

