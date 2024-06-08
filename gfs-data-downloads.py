#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wget

yearList = [str(y) for y in range(2022,2023)]  #for 2022 only
monthList = [str(f'{m:02}') for m in range(11,12)]  #for June, July, August, and September i.e., 06, 07, 08, 09 
dayList = [str(f'{d:02}') for d in range(22,23)]  # all days of the month
fileList = [str(f'{d:02}') for d in range(20,85)] # all files in the folder(0,85)

url='https://soostrc.comet.ucar.edu/data/grib/gfsp25/'
hoursOFdata=['00','06','12','18']
res='25'

for year in yearList:
    for month in monthList:
        for day in dayList:
            for file in fileList:
                for cy in hoursOFdata:
                    try:
                        print('\nDownloading: ' + url + year + month + day +'/grib.t' + cy + 'z/22'+ month + day + cy + '.gfs.t' + cy + 'z.0p' + res + '.pgrb2f0' +  file) 
                        wget.download(url + year + month + day +'/grib.t' + cy + 'z/22'+ month + day + cy + '.gfs.t' + cy + 'z.0p' + res + '.pgrb2f0' +  file)
                    except:
                        #if file is missed, skip it
                        print("\nData is missing. Skipping...%s" % url + year + month + day +'/grib.t' + cy + 'z/22'+ month + day + cy + '.gfs.t' + cy + 'z.0p' + res + '.pgrb2f0' +  file)
                        continue
