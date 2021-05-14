import arcpy
import os
arcpy.env.overwriteOutput=True
def workspace(workspace)
    #set workspace
    arcpy.env.workspace=workspace
#set new function to call desired fc
def airportsbuffer(fc, fields, in_features):
    #check to see if fc is in workspace
    if arcpy.Exists(fc):
        #curse through fc fields for desired variables
        with arcpy.da.SearchCursor(fc, fields) as cursor:
            for row in cursor:
                if row == "seaplane":
                    #buffer rows with criteria met and save into new shapefile
                    arcpy.analysis.Buffer(row, buffer_airports,"7500 METERS", "OUTSIDE_ONLY")
                if row == "airport"
                    #repeat buffer for new criteria
                    arcpy.analysis.Buffer(row, buffer_airports,"15000 METERS", "OUTSIDE_ONLY")
        
