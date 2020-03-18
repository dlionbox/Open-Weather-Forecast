import requests
import datetime
import time
import os
import pandas as pd
import numpy as np

# Example of the function with brazilian cities:

YOUR_API_KEY = "get the api key from the website in README"

# The name of the cities in a list:
cities_list = ["São Paulo", "Rio de Janeiro", "Porto Alegre"]
get_data(df, YOUR_API_KEY)


# The name of the cities in a DataFrame Pandas:
cities = df["Cities"].dropna().unique()
cities = pd.Series(cities)
cities.drop_duplicates(keep='first', inplace=True)

climate = get_data(cities, YOUR_API_KEY)
climate.head()
