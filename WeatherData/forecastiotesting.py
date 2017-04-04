import forecastio
import datetime as dt

api_key='e20dd4c7c92174bdca8d22b226e0bc6d'

lat =39.0119
lng = 98.4842

t = dt.datetime(2016, 7, 3)

forecast = forecastio.load_forecast(api_key, lat, lng, time=t, units="us")
data = forecast.json
print(data['daily']['data'][0])
for i in data['daily']['data'][0]:
  print(i)

print(data['daily']['data'][0]['temperatureMin'])
'''
for i in data:
  print(i)
  print('-------------------')
  print(data[i])
h = forecast.hourly()
#g = forecast.data
#for i in range(len(g)):
#  print(g[i])
'''
