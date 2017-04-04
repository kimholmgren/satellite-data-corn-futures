import pandas as pd
months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

class futuresData:
  
  def __init__(self, startYear, endYear):
    if(startYear<1980 or endYear>2017):
      raise ValueError("Only data between 1980 and 2017 is supported")


    self.startYear = startYear
    self.endYear = endYear
    futures_data = pd.read_csv('FuturesData/USCornFutures.csv')
    futures_data.set_index(futures_data['Date'], inplace=True)
    del futures_data['Date']
    yrs = {}
    for mon in months:
      curr = {}
      for yr in range(startYear, endYear):
        if(yr>2000):
          k = str(yr)[2:4]
          if(k[0]=='0'):
            k=k[1]
          curr[yr] = futures_data['Price'][k+'-'+mon]
        else:
          curr[yr]=futures_data['Price'][mon+'-'+str(yr)[2:4]]
      yrs[mon]=curr
    self.data = yrs
