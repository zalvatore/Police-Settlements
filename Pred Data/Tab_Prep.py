#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:22:30 2022

@author: salvadorsanchez
"""

import pandas as pd
import os


#Change Dir
dirstr = '/Users/salvadorsanchez/Dropbox/ADS/ADS 505 Applied Data Sci for Business/Tableau/police-settlements/'
os.chdir(dirstr)
list_dir = os.listdir(dirstr)

#Remove "."
list_dir = [x for x in list_dir if not '.' in x]

int_list = []

for directory in list_dir:
    try:
        list_dir_sub = os.listdir(dirstr + directory + '/final/')
        file = list_dir_sub[0]
        df = pd.read_csv(dirstr + directory + '/final/' + file)
        
        int_list = [y for x in [int_list, df.columns.tolist()] for y in x]

    except:
        pass

import numpy as np
  
  
def unique(list1):
    x = np.array(list1)
    return (np.unique(x))

col_names = unique(int_list)

df_data = pd.DataFrame(columns = col_names)


for directory in list_dir:
    try:
        list_dir_sub = os.listdir(dirstr + directory + '/final/')
        file = list_dir_sub[0]
        df = pd.read_csv(dirstr + directory + '/final/' + file)
        
        df_data = pd.concat([df_data ,df])

    except:
        pass

df_data.to_csv('Police_Data.csv')

