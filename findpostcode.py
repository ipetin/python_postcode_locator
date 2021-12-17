# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:17:39 2021

@author: iljap
"""
import csv
import json

from math import sin, cos, sqrt, atan2, radians

latlon_json_list_file = "latlonglist.json"
m100 = 0.00089997 #approx 100 meters in lanlon
km1 = m100*10

# test data
# postcode = "NW1 8NL" 
latitude= 51.540891
longitude= -0.142746

# postcode = "NW1 8QL" 
latitude2= 51.539288
longitude2= -0.142696

def reset():
    latitude = None 
    longitude = None
    latitude2 = None
    longitude2 = None
    

# calculate distance between two longitude and longitude points
if latitude and longitude and latitude2 and longitude2:
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(latitude)
    lon1 = radians(longitude)
    lat2 = radians(latitude2)
    lon2 = radians(longitude)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    print("Distance between two locations ", distance,'km' )
 

# radius distance to lookup postcodes from first lat lon provided
r = 0.1 #DEFAULT: within 100 meters

lonlat_json_list_file = "latlonglist.json"

# json file
if lonlat_json_list_file:
    #ignore all other input
    
    f = open(lonlat_json_list_file)

    data = json.load(f)

    for lonlat in data['lonlat']:
        # print(lonlati)
        latitude= float(lonlat[1])
        longitude=  float(lonlat[0])
        print(latitude,longitude)
    # Closing file
    # f.close()
        r_distance = r * km1
        lat_dist_up= round(latitude + r_distance,6)
        lat_dist_down= round(latitude - r_distance,6)
        lon_dist_up= round(longitude + r_distance,6)
        lon_dist_down= round(longitude - r_distance,6)
        
        with open('ukpostcodes.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # if not latlon_json_list_file:
            #     print("looking for latitude", latitude," r_distance",r_distance, "range:",lat_dist_up,lat_dist_down,"distance",lat_dist_up-lat_dist_down)
            
            for row in csv_reader:
                lat = float(row["latitude"])
                lon = float(row['longitude'])
                if r:
                  if lat <= lat_dist_up and lat >= lat_dist_down:
                      # print('postcode at lat:',str(lat),found_postcode,)
                      if lon <= lon_dist_up and lon >= lon_dist_down:
                           found_postcode = ''+row["postcode"]+''
                           print('> ',found_postcode,' lanlon:',str(lat),'',str(lon))
                           
            

