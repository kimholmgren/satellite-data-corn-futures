# satellite-data-corn-futures
# Purpose
This project is to explore using satellite imagery and weather data to predict corn futures, a task that is being taken on by many startups and trading firms to get an edge in the commodities pricing market.

# Contents
beginDownloads.sh - gets the .tif image from Google Earth Engine API - one image from each year in August with the NDVI filter applied
FuturesData - creates a class that gets data from the USCornFutures spreadsheet and puts it into an object
WeatherData - creates a class that gets data from the DarkSky API between a set start and end date over the summer and puts it into an object
SatelliteData - picks a location and date and gets one image per year using the NDVI filter (this calls beginDownloads.sh)

# Research
