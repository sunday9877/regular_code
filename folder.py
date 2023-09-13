#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:22:11 2021

@author: sangdi
"""

import os


parent_dir = "/data/disang/seviri/2018/m02/"
dat=180203

for i in range(25):
    dat1 = dat + i
    directory = str(dat1)
### create new directory
# # Parent Directory path

  
# # Path
    path1 = os.path.join(parent_dir, directory)
    os.mkdir(path1)
