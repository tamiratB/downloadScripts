#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:39:44 2020

@author: tamirat
Sample script to download ERA5 reanalysi soil moisture data from the Copernicus data repository.
"""

import cdsapi
import os

os.chdir('../../data/CdsData') # location to save the data 

c = cdsapi.Client()

yearlist = [str(y) for y in range(2001,2021)]
monthlist = [str(f'{m:02}') for m in range(1,13)]
daylist = [str(f'{d:02}') for d in range(1,32)]

for year in yearlist:

    c.retrieve(
        'reanalysis-era5-land',
        {
            'format': 'netcdf',
            'variable': [
            'volumetric_soil_water_layer_1',
        ],
            'year': year,
            'month': monthlist,
            'day': daylist,
	    'area': ['-40','-20','40','60'],   # African domain
            'time': [		               # 3 hourly data
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
			], 
		},
        'era5Land_soil_moisture_layer1_' + year + '.nc')
