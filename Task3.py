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


#Loop through BMR list to create new folders
for file in BMR:
    output_FC= f"V:\\ENV859_PS4\\Scratch\\{file}"
    arcpy.CreateFolder_management(output_FC, file)
    split_FC= 
    arcpy.Split_analysis(BMR(), split_FC, output_FC, "TriCounties")