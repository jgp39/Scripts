#set objects
streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFC = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
distance = arcpy.GetParameterAsText()

#create buffer 
arcpy.analysis.Buffer(streams,outFC,distance,"","","ALL")