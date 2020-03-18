# Open-Weather-Forecast
Function in python for getting forecast API calls in open weather website.

<p>In https://openweathermap.org/, create your account.
<p>https://home.openweathermap.org/api_keys gives you your API Key (necessary to run our function).

<p>The input of the function is a Pandas Series (<class 'pandas.core.series.Series'>) with the names of the cities to forecast.
<p>The output is a Pandas DataFrame, with 5 columns: 
  <p>Date (5 days forecast)
  <p>Description (how the climate is defined for the day - light rain, few clouds, broken clouds, ...
  <p>Temperature (in ºC)
  <p>Humidity (in %)
  <p>City (the name of the city)

<p>References:
<p>https://github.com/juhilsomaiya/API-Integrations-Python/tree/master/Weather_forecast
<p>https://pypi.org/project/yahoo-weather/
