#import modules
import arcpy, os, sys

arcpy.env.workspace = "V:\\ENV859_PS4\\Scratch"

#allow output files to be overwritten
arcpy.env.overwriteOutput = True


#set variables
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
distance = sys.argv[2]
outFC = "V:\\ENV859_PS4\\Scratch\\buff_{}m.shp".format(distance)



#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")
