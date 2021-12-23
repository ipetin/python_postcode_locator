# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:57:08 2021

@author: iljap
"""
import csv
import json
from geojson import Feature, FeatureCollection, Point, Polygon
from turfpy.measurement import points_within_polygon


def main():
    csvdb="ukpostcodes_full.csv"
    points_list = []
    lonlat_json_list_file = "import.json"
    export_file = "export.txt"
    f = open(lonlat_json_list_file)
    data = json.load(f)
    
    with open(csvdb, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("Loading files... ")
        lines= len(list(csv_reader))
        print(lines, "lines loaded")
        csv_file.close()
    
    ignored =0 
    saved = 0 
    with open(csvdb, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        _last_loaded=0.0
        _loaded=0
        for row in csv_reader:
            _loaded=_loaded+1
            lat = float(row["latitude"])
            lon = float(row["longitude"])


#TODO: Remove this ugly hack to save time and memory
            if round(lat,2)!=51.79 and round(lat,2)!=51.78 and round(lat,2)!=51.80:
                ignored=ignored+1
                continue
            if round(lon,2)!=-0.19 and round(lon,2)!=-0.20 and round(lon,2)!=-0.18 and round(lon,2)!=-0.21 :
                ignored=ignored+1
                continue  
                
          # $# import pdb; pdb.set_trace()
            point = Feature(geometry=Point((lat,lon)))
            points_list.append(point)
            saved=saved+1
            if(_last_loaded+0.003<round(_loaded/lines,3)):
                _last_loaded = round(_loaded/lines,3)
                print("caching "+str(round(_loaded/lines,3)*100)+"%")
        csv_file.close()

    points = FeatureCollection(points_list)
    print("cached",saved,"ignored",ignored)

    poligon_list = []
    print("creating polygon")
    for lonlat in data['lonlat']:
        lat = float(lonlat[1])
        lon = float(lonlat[0])
        poligon_list.append(tuple([lat,lon]))
    polyGon = Polygon([poligon_list])
    print("polygon created")

    
   
    print("finding points within polygon, this may take a few minutes depending on how big the database is, if its a .csv file it will take a while")
    result = points_within_polygon(points, polyGon)
    print("SEARCHING FOR POSTCODES WITHIN POLYGON")

    found =0 
    _loaded=0
    for row in result["features"]:
        latitude = row["geometry"]["coordinates"][0]
        longitude = row["geometry"]["coordinates"][1]
        r_distance = 0.00089997 
        lat_dist_up= round(latitude + r_distance,6)
        lat_dist_down= round(latitude - r_distance,6)
        lon_dist_up= round(longitude + r_distance,6)
        lon_dist_down= round(longitude - r_distance,6)
        with open(csvdb, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            _last_loaded=0.0
            _loaded=0
            for row in csv_reader:
                _loaded=_loaded+1
                lat = float(row["latitude"])
                lon = float(row["longitude"])
                
                if lat <= lat_dist_up and lat >= lat_dist_down:
                          if lon <= lon_dist_up and lon >= lon_dist_down:
                                found=found+1
                                export = open(export_file,"a")        # \n is placed to indicate EOL (End of Line)
                                export.write(row["postcode"]+ ' located at ' + str(lat)+":"+str(lon)+"\n") 
                                export.close() #to change file access mode
                                print('> ',row["postcode"],' lanlon:',str(lat),'',str(lon))
                                
                # if(_last_loaded+0.002<round(_loaded/saved,3)):
                #    _last_loaded = round(_loaded/saved,3)
                #    print("postcodes search "+str(round(_loaded/lines,3))+"%", found,"postcodes found")
            csv_file.close()   





if __name__ == '__main__':

    main() 
