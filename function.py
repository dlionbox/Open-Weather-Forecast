import requests
import datetime
import time
import os
import pandas as pd
import numpy as np

def get_data(cities, YOUR_API_KEY):
    app_id = YOUR_API_KEY
    dataset = pd.DataFrame(columns=["Date", "Description", "Temperature", "Humidity"])

    for i in cities:
        api_call = 'http://api.openweathermap.org/data/2.5/forecast?q=' + i + ',' + "BR" + '&appid=' + app_id + '&mode=json&units=metric'

        try:
            data = requests.post(api_call)
            humidity = []
            date = []
            temp = []
            desc = []

            data = data.json()

            for lists in data['list']:
                date.append(lists['dt_txt'])
                humidity.append(lists['main']['humidity'])
                temp.append(lists['main']['temp'])
                desc.append(lists['weather'][0]['description'])

            aux = pd.DataFrame({"Date": date, 
                                "Description": desc, 
                                "Temperature": temp, 
                                "Humidity": humidity, 
                                "City": i})
            dataset = dataset.append(aux)
            print(i+" Ok!")

        except:
            aux = pd.DataFrame({"Date": [""], 
                                "Description": ["Cidade não encontrada"], 
                                "Temperature": [np.nan], 
                                "Humidity": [np.nan], 
                                "City": [i]})
            dataset = dataset.append(aux)
            print(i+" Não encontrada na API!")

    return dataset
