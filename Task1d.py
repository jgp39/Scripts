#import modules
import arcpy, os, sys

arcpy.env.workspace = "V:\\ENV859_PS4\\Scratch"

#allow output files to be overwritten
arcpy.env.overwriteOutput = True


#set variables
streams = "V:\\ENV859_PS4\\Data\\streams.shp"


for i in range (5):
    distance = (sys.argv[1]),
    outFC = str("V:\\ENV859_PS4\\Scratch\\buff_"+ sys.argv[3] +"m.shp"),
    print(distance)



#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")


print(arcpy.GetMessages())