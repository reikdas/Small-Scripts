#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 20:07:01 2018

@author: pratyush
"""

#Removes html tags from a file

import os

path = input('Enter directory path of file : ')
file = input('Enter name of file : ')
if (path[len(path)-1] is not '/'):
    path = path+'/'
filename = path+file
f = open(filename, "r")
temporary = path+'temp.txt'
temp = open(temporary,"w+")
#Add tags as needed
tags = ['<html>','</html>','<body>','</body>','<head>','</head>']
for line in f:
    newline = ''
    for word in line.split():
        if word not in tags : 
            newline = newline + word + ' '
    if newline is not '' : 
        temp.write(newline+'\n')
os.remove(filename)
os.rename(temporary,filename)
temp.close()

