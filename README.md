# satellite-data-corn-futures
# Purpose
This project is to explore using satellite imagery and weather data to predict corn futures, a task that is being taken on by many startups and trading firms to get an edge in the commodities pricing market. There are many shortcomings of this implementation, which was just done to learn more about it and not for actual use. 

# Research
Chlorophyll strongly absorbs photosynthetically active radiation (PAR)/visible light (from .4 to .7 micrometers) while the cell structure of the leaves reflects near-infrared light (.7 to 1.1 micrometers). This is measured using NDVI, Normalized Difference Vegetation Index, which assesses the amount of live green vegetation. 

Weather variables – some are standard things to look at – ie temperature, amount of days clear, etc

Photosynthesis greatly reduced after in field temperatures reach a level of 85 to 90 degrees farenheit (30-32 celcius). 

Wide differences between daily min and max temps is associated w low levels of soil moisture.

Location choice:
https://ourworldindata.org/land-use-in-agriculture/
On the left is image from a paper by Max Roser on Land Use in Agriculture from 2008 U.S. Census of Agriculture and on the right highlighted in blue over an NDVI scaled colormap of the USA is the area I chose to examine (based on eyeballing the area with a high amount of corn crops)
![alt tag](https://github.com/kimholmgren/satellite-data-corn-futures/blob/master/readmeImages/locationChoice.png)



# Implementation 
![alt tag](https://github.com/kimholmgren/satellite-data-corn-futures/blob/master/readmeImages/myImplementation.png)


beginDownloads.sh - gets the .tif image from Google Earth Engine API - one image from each year in August with the NDVI filter applied
FuturesData - creates a class that gets data from the USCornFutures spreadsheet and puts it into an object. Source for data is https://www.investing.com/commodities/us-corn-historical-data
WeatherData - creates a class that gets data from the DarkSky API between a set start and end date over the summer and puts it into an object
SatelliteData - picks a location and date and gets one image per year using the NDVI filter (this calls beginDownloads.sh)

# Results 
See Analysis.ipnyb


