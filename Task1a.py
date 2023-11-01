###Set up
#save all files to Scrath folder using code below, plus 

import arcpy
#Task 1a
#set objects
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFC = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
distance = "1000 meters"

#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")

print(arcpy.GetMessages())