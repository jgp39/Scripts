###Task 1B: Setting the environment
import arcpy, os

streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFC = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
distance = "1000 meters"

#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")

arcpy.env.workspace = os.path.join("V:\\ENV859_PS4\\Data", streams)

#allow output files to be overwritten
arcpy.env.overwriteOutput = True

print(arcpy.GetMessages())