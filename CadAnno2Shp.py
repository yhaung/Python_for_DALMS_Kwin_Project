# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# CadAnno2Shp.py
# Created on: 2018-08-30 21:19:42.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# Cad annotation as point shp
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, os

# Local variables:
CadDir = "D:\\TAUNGOO_PILOT_TEST\\Python_test\\CadAnnoToShp\\"
#file = "k_585_b_myanmarno.dxf"
Anno ="\\Annotation"
ShpDir = "D:\\TAUNGOO_PILOT_TEST\\Python_test\\New folder"


for file in os.listdir(CadDir):
  if file.endswith(".dxf"):
	dxf = CadDir+file+Anno
	# Process: Feature Class To Shapefile (multiple)
	print (file + " is being converted" )
	arcpy.FeatureClassToShapefile_conversion(dxf, ShpDir)
	print (" ..done!" )
	
print ("Annotations to shp conversion complete")



