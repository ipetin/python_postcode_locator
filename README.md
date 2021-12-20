# python_postcode_locator
Get all postcodes from Latitude and Longitude in UK from import.json, OFFLINE.  
Exports postcodes with their geoposition to export.txt


HOW TO INSTALL:
Download UK Postcode .zip and extract ukpostcodes.csv it to python_postcode_locator root folder. 
This .csv will act as your database. Ideally you'll have a cached database to make searching faster.

https://www.freemaptools.com/download/full-uk-postcodes/ukpostcodes.zip

i suggest, openning the .csv and breaking it into 3-4 files as it will take a long time and do this multiple times on smaller .csv files.

-import.json contains postcode lists you want to find. Be sure that the last polygon coords end with the starting one as it has to lock connect

this is the polygon used in the example import.json provided


![Screenshot](https://github.com/ipetin/python_postcode_locator/blob/main/screenshot2.jpg)


-export.txt contains the found postcodes

RUN COMMAND TO FIND WITHIN POLYGON: 

python find_postcode_within_polygon.py

This will search for all postcodes within the polygon region specified in import.json


RUN COMMAND TO FIND POSTCODES CONNECTED TO THE ROAD (upto 100m) (Polygon boarders): 

python findpostcode.py


The output will be in export.txt


![Screenshot](https://github.com/ipetin/python_postcode_locator/blob/main/screenshot.jpg)



