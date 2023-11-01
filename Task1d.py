#import modules
import arcpy

arcpy.env.overwriteOutput = True

#set objects
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
distance = arcpy.GetParameterAsText()

#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")
