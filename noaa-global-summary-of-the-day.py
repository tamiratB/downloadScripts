
import wget

url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/archive/'

for year in range(1981, 2025):
    print('\nDownloading: ' + url + str(year) + '.tar.gz')
    wget.download(url + str(year) + '.tar.gz','/data/noaa-gsod/raw/' + str(year) + '.tar.gz')
