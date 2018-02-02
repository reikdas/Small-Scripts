#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:58:15 2018

@author: pratyush
"""

import os
path = input('Enter directory')
add = input('Enter the word to append to old filename')
files = os.listdir(path)

for file in files:
    newfile = file+add
    os.rename(os.path.join(path, file), os.path.join(path, newfile))