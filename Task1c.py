#import modules
import arcpy, os, sys

#allow output files to be overwritten
arcpy.env.overwriteOutput = True


#set variables
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFC = sys.argv[0]
distance = sys.argv[1]

arcpy.env.workspace = os.path.join("V:\\ENV859_PS4\\Data", streams)

#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")


print(arcpy.GetMessages())