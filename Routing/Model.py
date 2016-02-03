# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Model.py
# Created on: 2015-11-12 17:32:52.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("Network")


# Local variables:
New_York_Network_ND = "New_York_Network_ND"
Graffiti_111015 = "G:\\MGIS\\Maps\\AM\\Graffiti_111015\\Data\\Graffiti_111015.mdb\\Graffiti_111015"
Graffiti_111015__2_ = "Graffiti_111015"
Route = "Route"
Graffiti_111015__3_ = "Graffiti_111015"
Route__3_ = "Route"

# Process: Make Route Layer
arcpy.MakeRouteLayer_na(New_York_Network_ND, "Route", "Cost", "FIND_BEST_ORDER", "PRESERVE_NONE", "NO_TIMEWINDOWS", "", "ALLOW_UTURNS", "Oneway", "USE_HIERARCHY", "", "TRUE_LINES_WITH_MEASURES", "")

# Process: Make XY Event Layer
arcpy.MakeXYEventLayer_management(Graffiti_111015, "xcoord", "ycoord", Graffiti_111015__2_, "", "")

# Process: Calculate Locations
arcpy.CalculateLocations_na(Graffiti_111015__2_, New_York_Network_ND, "5000 Meters", "New_York_Network SHAPE;New_York_Network_ND2_Junctions NONE", "MATCH_TO_CLOSEST", "", "", "", "", "", "", "", "", "Locations", "INCLUDE", "New_York_Network #;New_York_Network_ND2_Junctions #")

# Process: Add Locations
arcpy.AddLocations_na(Route, "Stops", Graffiti_111015__3_, "Name Service_Request_ #", "5000 Meters", "", "New_York_Network SHAPE;New_York_Network_ND2_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "New_York_Network #;New_York_Network_ND2_Junctions #")

# Process: Solve
arcpy.Solve_na(Route__3_, "HALT", "CONTINUE", "")
