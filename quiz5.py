def(input_geodatabase, fcPolygonA, fcPolygon B):
    import arcpy
    import os
    arcpy.env.workspace=input_geodatabase
    #set variables
    PolygonA="fcPolygonA" #block_groups
    PolygonB="fcPolygonB" #parks
    outputIntersect="outputfc"

    #add field for polygon A area and then calculate area
    arcpy.AddField_management(PolygonA, "areafieldA","field_type")
    arcpy.CalculateGeometryAttributes_management(PolygonA,[["areafieldA","geometry_propery"]],"area_unit")
    #Evaluate area in common
    arcpy.Intersect_analysis([PolygonA, Polygon B],"output_intersect")
    #Add field for area in common and calculate area
    areafieldAB="areafieldAB"
    arcpy.AddField_management(outputIntersect,"areafieldAB","field_type")
    arcpy.CalculateGeometryAttributes_management(outputIntersect, [[areafieldAB, "geometry_property"]], "area_unit")
    #create dictionary and cursor to add field column up
    output_dict = dict()
    with arcpy.da.SearchCursor(outputIntersect, ["field",areafieldAB]) as cursor:
        for row in cursor:
            field = row[0]
            if field in output_dict.keys():
                output_dict[field] += row[1]
            else:
                output_dict[field] = row[1]    
    #not sure what this part does
    with arcpy.da.UpdateCursor(block_groups, ["field", area_field]) as cursor:
        for row in cursor:
            if row[0] in output_dict.keys():
                row[1] = output_dict[row[0]]
            else:
                row[1] = 0
            cursor.updateRow(row)
    #create field for percentage
    pct_field = "pct"
    arcpy.AddField_management(PolygonA,pct_field, "field_type")
    #Calculate percentage and append to percent field
    arcpy.CalculateField_management(outputIntersect, pct_field, "!areafieldA!/!areafieldAB!", "PYTHON3")
