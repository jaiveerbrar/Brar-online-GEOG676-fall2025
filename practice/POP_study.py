import arcpy
source = r"C:/Users/jaiveer.brar/OneDrive - Texas A&M AgriLife/Plant pop study/Rasters/5.20.25/"
band1 = arcpy.sa.Raster(source + "B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "B2.TIF") # green
band3 = arcpy.sa.Raster(source + "B3.TIF") # red
band4 = arcpy.sa.Raster(source + "B4.TIF") # NIR
#composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "combined.tif")

ndvi = ((band4 - band3) / (band4 + band3))
ndvi.save(source + "ndvi.tif")