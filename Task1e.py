#import modules
import arcpy, os, sys

arcpy.env.workspace = "V:\\ENV859_PS4\\Scratch"

#allow output files to be overwritten
arcpy.env.overwriteOutput = True


#set variables
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
distance = ["100", "200" ,"300", "400","500"]

for i in distance:
    outFC = "V:\\ENV859_PS4\\Scratch\\buff_{}m.shp".format(distance)



#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")


#dont use a json file for 4 & 5  