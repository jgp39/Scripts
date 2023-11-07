import arcpy

arcpy.env.workspace= "V:\\ENV859_PS4\\Data"
#user input for Feature Class and Field Name
feature_class= arcpy.GetParameterAsText(0)
field_name= arcpy.GetParameterAsText(1)

#Creating my own point
myPoint= arcpy.Point(X=621000,Y=254000)

#Creating my own SearchCursor
with arcpy.da.SearchCursor(feature_class, ['Shape@', field_name]) as cursor:
    for i in cursor:
        recShape,field_value = i
        if recShape is not None and recShape.contains(myPoint):
            arcpy.AddMessage(f"The field's value is {field_value}.")
