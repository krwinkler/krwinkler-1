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
# Problem 1: 20 Points
#
# Given a csv file import it into the database passed as in the second parameter
# Each parameter is described below:

# csvFile: The absolute path of the file should be included (e.g., C:/users/ckoylu/test.csv)
# geodatabase: The workspace geodatabase
###################################################################### 
import arcpy
import os
arcpy.env.overwriteOutput = True
    def importCSVIntoGeodatabase(csvFile, geodatabase):
        #set workspace
        arcpy.env.workspace=geodatabase
        #limit field returns by stationID
        expression=arcpy.AddFieldDelimiters(arcpy.env.workspace, "stationID") + " <> 'IA0000'"
        #check if file exists
        if arcpy.Exists(csvFile):
            #only complete import if file exists
            arcpy.TableToTable_conversion(intable,geodatabase, "CSVtable", expression)
        

##################################################################################################### 
# Problem 2: 80 Points Total
#
# Given a csv table with point coordinates, this function should create an interpolated
# raster surface, clip it by a polygon shapefile boundary, and generate an isarithmic map

# You can organize your code using multiple functions. For example,
# you can first do the interpolation, then clip then equal interval classification
# to generate an isarithmic map

# Each parameter is described below:

# inTable: The name of the table that contain point observations for interpolation       
# valueField: The name of the field to be used in interpolation
# xField: The field that contains the longitude values
# yField: The field that contains the latitude values
# inClipFc: The input feature class for clipping the interpolated raster
# workspace: The geodatabase workspace

# Below are suggested steps for your program. More code may be needed for exception handling
#    and checking the accuracy of the input values.

# 1- Do not hardcode any parameters or filenames in your code.
#    Name your parameters and output files based on inputs. For example,
#    interpolated raster can be named after the field value field name 
# 2- You can assume the input table should have the coordinates in latitude and longitude (WGS84)
# 3- Generate an input feature later using inTable
# 4- Convert the projection of the input feature layer
#    to match the coordinate system of the clip feature class. Do not clip the features yet.
# 5- Check and enable the spatial analyst extension for kriging
# 6- Use KrigingModelOrdinary function and interpolate the projected feature class
#    that was created from the point feature layer.
# 7- Clip the interpolated kriging raster, and delete the original kriging result
#    after successful clipping. 
#################################################################################################################### 
    def krigingFromPointCSV(inTable, valueField, xField, yField, inClipFc, workspace = "assignment3.gdb"):
        #Map longitude and latitude from table
        arcpy.management.XYTableToPoint(intable, "year", x_field, y_field)
            #check extension before using
            try:
                if arcpy.CheckExtension("Spatial") == "Available":
                    arcpy.CheckExtension("Spatial")
                else:
                    raise LicenseError:
                        print("Spatial Analyst License is unavailable")
        #describe year features
        desc= arcpy.Describe("year")
        #set variable cellsize to 0
        CellSize= 0
        #set width and height 
        width = desc.extent.width
        height= desc.extent.height
        if width < height:
            CellSize = width / 1000
        else:
            CellSize = height / 1000
        #set ooutput name for variable
        field="F2018_PREC"
        #perform Kriging dataset and save
        outKriging = Kriging("year", field, '#', CellSize)
        outKriging.save("F2018k")
        #Describe clip fc and set variable rectangle to equal it's extent
        descClip = arcpy.Describe(inClipFc)
        rectangle = str(descClip.extent.XMin) + " " + str(descClip.extent.YMin) + " " + str(descClip.extent.XMax) + " " + str(descClip.extent.YMax)
        #clip raster
        arcpy.Clip_management(outKriging, rectangle, "F2018KC", inClipFc, "#", "ClippingGeometry", "MAINTAIN_EXTENT" )
        #change integer to floating point raster
        outInt = Int("F2018KC")
        outInt.save("F2018KCI")
        #find minimum and maximum values of outInt
        min_F2018 = arcpy.management.GetRasterProperties(outInt, "MINIMUM")
        max_F2018 = arcpy.management.GetRasterProperties(outInt, "MAXIMUM")
        #variable to number of classes
        numofclasses = 5
        #find class range for equal interval breaks
        eq_interval = (int(max_F2018.getOutput(0)) - int(min_F2018.getOutput(0))) / numofclasses
        #empty list
        remapRangeList = []
        mybreak = int(min_F2018.getOutput(0))
        #create loop to make list with lower, upper, and class number for each of 5 classes
        for l in range(0, numofclasses):
            newClassCode = l + 1
            lowerBound = mybreak
            upperbound = mybreak + eq_interval
            remap = [lowerBound, upperbound, newClassCode]
            remapRangeList.append(remap)
            mybreak += eq_interval
        #reclassify raster into isarithmic map
        outReclassRR = Reclassify("F2018KCI", "Value", RemapRange(remapRangeList), "NODATA")
        outReclassRR.save("F2018_CL")
        #convert tto polygon
        arcpy.RasterToPolygon_conversion("F2018_CL", "F2018_ismc")
        

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
