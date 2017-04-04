import forecastio
import datetime as dt


class weatherData :

  #by default choose center of kansas for latitude and longtitude
  #this will get weather data between the startDate and stopDate for yearStart to yearStop
  #at location (lat, long)
  def __init__(self, startDate, stopDate, lat=39.0119, lng=98.4842):
    self.startDate = startDate
    self.stopDate = stopDate
    self.lat = lat
    self.long = lng
    self.data = {}
    self.api_key='e20dd4c7c92174bdca8d22b226e0bc6d'
    for yr in range(stopDate.year-startDate.year):
      n = startDate.year + yr
      print("Collecting weather data for the year "+str(n)+" between "+str(startDate)+" and "+str(stopDate)+".")
      currYr = self.processYear(n)
      self.data[startDate.year+yr] = currYr

  def processYear(self, currYr):
    #initialize all variables to 0
    avgTemp = 0
    minTemp = 0
    maxTemp = 0
    pctOver88 = 0
    pctClear = 0
    avgHumid = 0
    avgPressure = 0
    avgDewPoint = 0
    avgPctCover = 0
    ctr = 0

    thisStart = dt.datetime(currYr, self.startDate.month, self.startDate.day)
    thisEnd = dt.datetime(currYr, self.stopDate.month, self.stopDate.day)

    #loop through each date and update values
    for currDate in self.daterange(thisStart, thisEnd):
      try:
        forecast = forecastio.load_forecast(self.api_key, self.lat, self.long, time=currDate, units="us")
        data=forecast.json
        ctr+=1
        avgTemp+=data['daily']['data'][0]['temperatureMin']*.33 + data['daily']['data'][0]['temperatureMax']*.67
        minTemp = min(minTemp, data['daily']['data'][0]['temperatureMin'])
        maxTemp = max(maxTemp, data['daily']['data'][0]['temperatureMax'])
        if(data['daily']['data'][0]['temperatureMax']>88):
          pctOver88+=1
        if(data['daily']['data'][0]['icon']=='clear-day'):
          pctClear+=1
        avgHumid += data['daily']['data'][0]['humidity']
        avgPressure += data['daily']['data'][0]['pressure']
        avgDewPoint += data['daily']['data'][0]['dewPoint']
        avgPctCover += data['daily']['data'][0]['cloudCover']
      except KeyError as k:
        print("Key "+str(k)+" not found. "+str(currDate)+" ommitted from calculation.")
        continue



    #finalize computations
    avgTemp = avgTemp/ctr
    minMaxTemp = maxTemp - minTemp
    pctOver88 = pctOver88/ctr
    pctClear = pctClear/ctr
    avgHumid = avgHumid/ctr
    avgPressure = avgPressure/ctr
    avgDewPoint = avgDewPoint/ctr
    avgPctCover = avgPctCover/ctr

    #create a dict to store
    ret = {}
    ret['avgTemp'] = avgTemp
    ret['minMaxTemp'] = minMaxTemp
    ret['pctOver88'] = pctOver88
    ret['pctClear'] = pctClear
    ret['avgHumid'] = avgHumid
    ret['avgPressure'] = avgPressure
    ret['avgDewPoint'] = avgDewPoint
    ret['avgPctCover'] = avgPctCover
    return ret


  #daterange from stackoverflow at http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
  def daterange(self, start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
      yield start_date + dt.timedelta(n)




