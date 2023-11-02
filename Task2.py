#set up environment
import arcpy, sys, os

arcpy.env.OverwriteOutput = True

#define variables
roads = "V:\\ENV859_PS4\\Data\\Roads.shp"
road_type = "0;201;203"
road_types= ["0", "201", "203"]

#loop through variables and selects features
for i in roads:
    



