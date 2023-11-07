#import modules and set up env
import arcpy


#indicate catalogPath property
dataset= arcpy.GetParameterAsText(0)

try:
    desc= arcpy.Describe(dataset)


    #User input for Min and Max values
    XMin = round(desc.extent.XMin,1)
    YMin = round(desc.extent.YMin,1)
    XMax = round(desc.extent.XMax,1)
    YMax = round(desc.extent.YMax,1)
    arcpy.AddMessage(f"XMin: {XMin}\nYMin: {YMin}\nXMax: {XMax}\nYMax: {YMax}")

    #Report on dataset
    if desc.datasetType == "FeatureClass":
        arcpy.AddWarning("Feature Type: " + desc.featureType)
    elif desc.datasetType == "RasterDataset":
        arcpy.AddWarning("Raster Format: %s, Rows:%s, Columns: %s" %(desc.format, desc.height, desc.width))
    else:
        arcpy.AddError(f"The dataset is a {type}.")

except arcpy.ExecuteError:
    arcpy.AddError(arcpy.GetMessages())

except Exception as e:
    arcpy.AddError(str(e))

##I used a significant amount of ChatGPT and google to assist me with this Task. Due to the hours I was up working on this, there was no one around me to ask for assistance. 