#set up environment
import arcpy, sys, os

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "V:\\ENV859_PS4\\Scratch"

#define variables
roads = "V:\\ENV859_PS4\\Data\\Roads.shp"
road_type = "0;201;203"
road_types= road_type.split(";")



#loop through variables and selects features
for i in road_types:
    outFC = f"V:\\ENV859_PS4\\Scratch\\roads_{i}.shp"
    where_clause = f'"ROAD_TYPE" = {i}'
    arcpy.analysis.Select(roads, outFC, where_clause)



# I had to use ChatGPT to assist me in this section. I don't understand what I am doing at all and the videos and examples were not helping and neither was asking my peers. So to 
#trouble shoot my issues I used ChatGPT to get a better understanding. I was also unable to ask the professor or TA because they were both away on the day I was working on this. 