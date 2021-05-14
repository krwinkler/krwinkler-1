###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Katelyn Winkler", "krwinkler"])

###################################################################### 
# Problem 1 (20 points)
# 
# Given an input point feature class (e.g., facilities or hospitals) and a polyline feature class, i.e., bike_routes:
# Calculate the distance of each facility to the closest bike route and append the value to a new field.
#        
###################################################################### 
import arcpy
import os
def calculateDistanceFromPointsToPolylines(input_geodatabase, fcPoint, fcPolyline):
    #set workspace
    arcpy.env.workspace=input_geodatabase
    #calculate distance to nearest route and append
    arcpy.analysis.Near(fcPoint, fcPolyline)

######################################################################
# Problem 2 (30 points)
# 
# Given an input point feature class, i.e., facilities, with a field name (FACILITY) and a value ('NURSING HOME'), and a polygon feature class, i.e., block_groups:
# Count the number of the given type of point features (NURSING HOME) within each polygon and append the counts as a new field in the polygon feature class
#
######################################################################
def countPointsByTypeWithinPolygon(input_geodatabase, fcPoint, pointFieldName, pointFieldValue, fcPolygon):
    #set workspace
    arcpy.env.workspace=input_geodatabase
    #set variable to equal results of SelectLayerByAttributte_management using SQL clause
    nursing_homes = arcpy.SelectLayerByAttribute_management(fcPoint, "NEW_SELECTION", "pointFieldName = pointFieldValue")
    #Find number of points within desired polygon
    arcpy.analysis.SummarizeWithin(fcPolygon, nursing_homes, "out_feature_class")

######################################################################
# Problem 3 (50 points)
# 
# Given a polygon feature class, i.e., block_groups, and a point feature class, i.e., facilities,
# with a field name within point feature class that can distinguish categories of points (i.e., FACILITY);
# count the number of points for every type of point features (NURSING HOME, LIBRARY, HEALTH CENTER, etc.) within each polygon and
# append the counts to a new field with an abbreviation of the feature type (e.g., nursinghome, healthcenter) into the polygon feature class 

# HINT: If you find an easier solution to the problem than the steps below, feel free to implement.
# Below steps are not necessarily explaining all the code parts, but rather a logical workflow for you to get started.
# Therefore, you may have to write more code in between these steps.

# 1- Extract all distinct values of the attribute (e.g., FACILITY) from the point feature class and save it into a list
# 2- Go through the list of values:
#    a) Generate a shortened name for the point type using the value in the list by removing the white spaces and taking the first 13 characters of the values.
#    b) Create a field in polygon feature class using the shortened name of the point type value.
#    c) Perform a spatial join between polygon features and point features using the specific point type value on the attribute (e.g., FACILITY)
#    d) Join the counts back to the original polygon feature class, then calculate the field for the point type with the value of using the join count field.
#    e) Delete uncessary files and the fields that you generated through the process, including the spatial join outputs.  
######################################################################
def countCategoricalPointTypesWithinPolygons(fcPoint, pointFieldName, fcPolygon, workspace):
    arcpy.env.workspace=workspace
    #set empty list to appent distinct values to
    list=[]
    #Generate distinct values and save into list by using search cursor
    with arcpy.da.SearchCursor(fcpoint, pointFieldName)as cursor:
        for row in cursor:
            if row not in list:
                list.append(row)
            else:
                pass
    #For each name in list generate shortened name and remove white spaces
    for l in list:
        for i in l:
            l.replace(" " "")
            #add field with new name
            arcpy.management.AddField(fcpolygon, l[0:12], "DOUBLE")
            #join polygon features and point feaures
            arcpy.analysis.SpatialJoin(fcpoint, fcPolygon, "output")
            #calculate field for point type
            arcpy.analysis.SummarizeWithin(fcPolygon, "output", "out_feature_class")
            #delete unnecessary spatial join output
            arcpy.management.Delete("output")
    
    
        
        
        
    

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
