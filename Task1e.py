#import modules
import arcpy, os, sys

arcpy.env.workspace = "V:\\ENV859_PS4\\Scratch"

#allow output files to be overwritten
arcpy.env.overwriteOutput = True


#set variables
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
distance = [100, 200, 300, 400, 500]

for distance in range (5):
    distance[+1],
    outFC = str("V:\\ENV859_PS4\\Scratch\\buff_"+ distance +"m.shp"),
    #create buffer 
    arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")


print(arcpy.GetMessages())