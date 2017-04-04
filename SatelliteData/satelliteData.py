import datetime
import ee
import ee.mapclient
import subprocess
from PIL import Image
import numpy as np


class satelliteData:
  def __init__(self, startDate, endDate):
    self.startDate = startDate
    self.endDate = endDate
    self.run()


  def run(self):
    startYear = self.startDate
    endYear = self.endDate
    self.data = {}
    ee.Initialize()
    #define the shape to look at
    polygon = ee.Geometry.Polygon([[[-98.701171875,37.82280243352756], [-99.4921875,34.41597338448186], [-89.912109375,33.8339199536547], [-88.681640625,35.20972164522138], [-83.759765625,37.61423141542417], [-85.78125,40.34654412118006], [-93.427734375,41.34382458118569], [-96.240234375,38.51378825951165], [-98.701171875,37.82280243352756]]])
    #initialize file to write URLs to
    f = open("beginDownloads.sh", "w")
    #get NDVI for each year
    for year in range(startYear, endYear):
      print("Finding NDVI image for "+str(year))
      img = ee.Image('MOD09GA/MOD09GA_005_'+ str(year) + '_08_01')
      ndvi = NDVI(img)
      clipped = ndvi.clip(polygon)
      url = "'" + clipped.getDownloadURL() +"'"
      f.write("wget " + url + " -O download"+str(year)+".zip\n")
      f.write('unzip download'+str(year)+'.zip\n')
      f.write('mv *.nd.tif '+str(year)+'.tif\n')
      f.write('\n')
      

    f.write('for file in download*; do rm $file; done\n')
    f.write('rm *tfw')
    f.close()
    print("Downloading all images locally")
    subprocess.call(['bash', 'beginDownloads.sh'])
    for year in range(startYear, endYear):
      self.data[year] = np.array(Image.open(str(year)+'.tif'))





def NDVI(image):
  return image.normalizedDifference(['sur_refl_b02', 'sur_refl_b01'])

def SAVI(image):
  return ee.Image(0).expression(
    '(1 + L) * float(nir - red)/ (nir + red + L)',
    {
        'nir': image.select('B4'),
        'red': image.select('B3'),
        'L': 0.2
    })      
