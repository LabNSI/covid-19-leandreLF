############################################
#
# Trace graphs
# Author : MS
# Date : 16/03/2020
# Update : 09/01/2022
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv
import matplotlib.pyplot as plt
from covid19v1 import *
from covid19v2 import *
from covid19v3 import *


def trace_data_for_country(country):
    '''
    Prepare lists of datas for x and y axis
    '''
    # x is an empty list
    x = []
    # y is an empty list
    y = []
    # browse through the country dictionary to get datas.
    # - Keys contain dates
    # - Values contain datas for y axis (number of daily cases)
    # x axis contains the number of days since the beginning of pandemic
    day = 0

    #for key, value in the country dictionnary
    for key, value in country.items():
        # Filter inappropriate keys
        if key != 'Province/State' and key !='Country/Region' and key != 'Lat' and key != 'Lon':
            # Add day number to the x list
            x.append(day)
            # Prepare for the next day
            day = day+1
            # add value to the y list.
            # value must be a number
            y.append(float(value))
    # return a tuple of lists x,y
    return x,y

        
# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_19-covid-Confirmed.csv"
    # where datas are located
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
        countries = read_CSV(file)
        
        chine = data_for_country(countries, 'Hubei', 'China')
        france = data_for_country(countries, '', 'France')
        italie = data_for_country(countries, '', 'Italy')
        japon = data_for_country(countries, '', 'Japan')

        
        print(chine)
        print(france)
        print(italie)
        print(japon)
        
        # Figure dimensions
        plt.figure(figsize=(10, 7))


        # Plot datas for China
        x , y = trace_data_for_country(chine)
        plt.plot(x, y, label="Chine")

        # Plot datas for France
        x , y = trace_data_for_country(france)
        plt.plot(x, y, label="France")

        # Plot datas for Italy
        x , y = trace_data_for_country(italie)
        plt.plot(x, y, label="Italie")


        x , y = trace_data_for_country(japon)
        plt.plot(x, y, label="Japon")

        

        # Add title to graph : "Infectés COVID-19 depuis le 22/01/2020"
        plt.title('Infectés COVID-19 depuis le 22/01/2020')

        # Add label on x axis : 'Nombre de jours'
        plt.xlabel('Nombre de jours')

        # Add label on y axis : 'Nombre de contaminés'
        plt.ylabel('Nombre de contaminés')

        # Add legend to graph
        plt.legend()

        # Save the figure as an image
        plt.savefig('covid19-Confimed.png')
        
        # Show graph
        plt.show()
        
        # Close graph
        plt.close()
        
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





