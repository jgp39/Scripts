import arcpy

arcpy.env.workspace= "V:\\ENV859_PS4\\Data"
#user input for Feature Class and Field Name
feature_class= arcpy.GetParameterAsText(0)
field_name= arcpy.GetParameterAsText(1)

#Creating my own point
myPoint= arcpy.Point(X=621000,Y=254000)

#Creating my own SearchCursor
lookup = arcpy.da.SearchCursor(feature_class, ['SHAPE@', field_name])

#for i in lookup:
 #   recShape = 'Shape@'
  #  print(feature.contains(myPoint))