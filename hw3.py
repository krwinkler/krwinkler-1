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
import arcpy
import os
###################################################################### 
# Problem 1 (10 Points)
#
# This function reads all the feature classes in a workspace (folder or geodatabase) and
# prints the name of each feature class and the geometry type of that feature class in the following format:
# 'states is a point feature class###################################################################### 
def printFeatureClassNames(workspace):
    #set workspace
    arcpy.env.workspace= workspace
    #set variable for ListFeatureClass function
    fclasses = arcpy.ListFeatureClasses()
    #create for loop to curse through 
    for fclass in fclasses:
        fctype = arcpy.Describe(fclass).shapeType
        print "{0} is a {1} feature class".format(fclass, fctype)

#printFeatureClassNames(r"C:\Users\Krwinkler\Downloads\hw3.dgb")

###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):
    #set workspace
    arcpy.env.workspace = workspace
    #create list variable to  attribute names
    fieldList = arcpy.env.ListFields(featureClass)
    for field in fieldList:
        if field.type == int or field.type == float or field.type == double
        print "{0} is a {1} type".format(field.name, field.type)

###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    arcpy.env.workspace=input_geodatabase #or any file geodatabase as workspace
    abspath=os.path.abspath(input_geodatabase)
    dir_folder=os.path.dirname(abspath)
    arcpy.CreateFileGDB_management(dir_folder, output_geodatabase)
   
    fc_list = arcpy.ListFeatureClasses('*', shapeType) #some shapetype here
    for fc in fc_list:
        arcpy.CopyFeatures_management(fc, output_geodatabase+'/'+fc)

#exportFeatureClassesByShapeType(r"C:\Users\Krwinkler\Downloads\hw3.dgb",'polygon',"hw3output.gdb")

###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
arcpy.env.workspace=workspace
outTable=arcpy.JoinField_management(inputFc, idFieldInputFc,inputTable, idFieldTable)
arcpy.CopyFeature_management(outTable, "newFC")


######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
