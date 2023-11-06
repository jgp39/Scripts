# set up environment and modules
import arcpy, sys, os

arcpy.env.workspace= "V:\\ENV859_PS4\\Data"

#Check to see if ArcPy is using ArcInfo
if arcpy.CheckProduct("ArcInfo") =="Available":
    print("ArcPy is using ArcInfo")
else:
    print("Proper licensing is not available.")

#create a list with all BMR feature classes
BMR = arcpy.ListFeatureClasses("BMR*")

output_FC= "V:\\ENV859_PS4\\Scratch"

#Loop through BMR list to create new folders
for file in BMR:
    filename= file[:-4]
    arcpy.management.CreateFolder(output_FC, filename)
    input_FC= file
    arcpy.Split_analysis(input_FC,"V:\\ENV859_PS4\\Data\\TriCounties.shp", "CO_NAME", output_FC, )