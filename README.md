# Open-Weather-Forecast
Function in python for getting forecast API calls in open weather website.

In https://openweathermap.org/, create your account.
https://home.openweathermap.org/api_keys gives you your API Key (necessary to run our function).

The input of the function is a Pandas Series (<class 'pandas.core.series.Series'>) with the names of the cities to forecast.
The output is a Pandas DataFrame, with 5 columns: 
  Date (5 days forecast)
  Description (how the climate is defined for the day - light rain, few clouds, broken clouds, ...
  Temperature (in ºC)
  Humidity (in %)
  City (the name of the city)

References:
https://github.com/juhilsomaiya/API-Integrations-Python/tree/master/Weather_forecast
https://pypi.org/project/yahoo-weather/
