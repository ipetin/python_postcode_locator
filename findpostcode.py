# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:17:39 2021

@author: iljap
"""
import csv
import json

from math import sin, cos, sqrt, atan2, radians


m100 = 0.00089997 


# radius distance to lookup postcodes from first lat lon provided

lonlat_json_list_file = "import.json"
export_file = "export.txt"
# json file
if lonlat_json_list_file:
    #ignore all other input
    
    r = 1 #DEFAULT: within 100 meters    
    f = open(lonlat_json_list_file)

    data = json.load(f)

    for lonlat in data['lonlat']:
        latitude= float(lonlat[1])
        longitude=  float(lonlat[0])
        r_distance = r * m100
        lat_dist_up= round(latitude + r_distance,6)
        lat_dist_down= round(latitude - r_distance,6)
        lon_dist_up= round(longitude + r_distance,6)
        lon_dist_down= round(longitude - r_distance,6)
        postcodes=[]
        with open('ukpostcodes.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                lat = float(row["latitude"])
                lon = float(row['longitude'])
                if r:
                  if lat <= lat_dist_up and lat >= lat_dist_down:

                      if lon <= lon_dist_up and lon >= lon_dist_down:
                           export = open(export_file,"a")        # \n is placed to indicate EOL (End of Line)
                           export.write(row["postcode"]+ "\n") 
                           export.close() #to change file access mode
                           print('> ',row["postcode"],' lanlon:',str(lat),'',str(lon))
            csv_file.close()

                                   
            
            
            
            

