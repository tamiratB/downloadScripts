#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:16:30 2020
"""
import wget
import os

url='https://data.giss.nasa.gov/impacts/agmipcf/agmerra/'

for year in range(1980,2011):
    for var in ['prate','rhstmax','srad','tavg','tmax','tmin','wndspd']:
        if os.path.isfile('/data/AgMERRA/raw/AgMERRA_' + str(year) + '_' + var + '.nc4'):  #if file exists, loop back
            print('\nCompleted!: ' + url + 'AgMERRA_' + str(year) + '_' + var + '.nc4')
            continue
        else:
            print('\nDownloading: ' + url + 'AgMERRA_' + str(year) + '_' + var + '.nc4')
            wget.download(url + 'AgMERRA_' + str(year) + '_' + var + '.nc4','/data/AgMERRA/raw/AgMERRA_' + str(year) + '_' + var + '.nc4')