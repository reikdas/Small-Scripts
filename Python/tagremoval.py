#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 20:07:01 2018

@author: pratyush
"""

#Removes html tags from a file

import os
import bleach 

path = input('Enter directory path of file : ')
file = input('Enter name of file : ')
if (path[len(path)-1] is not '/'):
    path = path+'/'
filename = path+file
f = open(filename, "r")
temporary = path+'temp.txt'
temp = open(temporary,"w+")
for line in f:
    newline = bleach.clean(line, tags=[], attributes={}, styles=[], strip=True)
    temp.write(newline+'\n');
os.remove(filename)
os.rename(temporary,filename)
temp.close()

