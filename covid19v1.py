############################################
#
# Download a file
# Author : MS
# Date : 16/03/2020
# update : 09/01/2022
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2

def download_file(url, file_name):
    '''
    Download a file from url and copy it localy with file_name as name
    '''
    try:
        # open url passed in argument
        file = urllib2.urlopen(url)
        # open file for writing in binary mode
        # https://docs.python.org/3/library/functions.html#open
        with open(file_name, 'wb') as output:
            # write in output the file read
            # use write and read functions
            output.write(file.read())
        # OK : return true
        return True
    except:
        # Something is wrong : return false
        return False
     
# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_19-covid-Confirmed.csv"
    # where datas are located
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
    else:
        print(f'Téléchargement du fichier {file} impossible')
