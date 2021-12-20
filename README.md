# python_postcode_locator
Get all postcodes from Latitude and Longitude in UK from import.json, OFFLINE.  
Exports postcodes with their geoposition to export.txt


HOW TO INSTALL:
Download UK Postcode .zip and extract ukpostcodes.csv it to python_postcode_locator root folder. 
This .csv will act as your database. Ideally you'll have a cached database to make searching faster.

https://www.freemaptools.com/download/full-uk-postcodes/ukpostcodes.zip

-import.json contains postcode lists you want to find. Be sure that the last polygon coords end with the starting one as it has to lock connect

-export.txt contains the found postcodes

RUN COMMAND TO FIND WITHIN POLYGON: 

python find_postcode_within_polygon.py

This will search for all postcodes within the polygon region specified in import.json


RUN COMMAND TO FIND POSTCODES CONNECTED TO THE ROAD (Polygon boarders): 

python findpostcode.py


The output will be in export.txt


![Screenshot](https://github.com/ipetin/python_postcode_locator/blob/main/screenshot.jpg)



