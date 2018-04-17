import numpy as n
import os
from osgeo import gdal
from osgeo import gdalconst

# Set paths to search for layers
path = "c:\\lab7\\"
landsatFile = path + "landsat\\"

try:
#gets a list of the files in the path
    files = os.listdir(landsatFile)
except:
    print(
        "Cannot find the landsat folder path".format(landsatFile))
    exit()

# Grab the right files with the red (band 3) and Near-IR (band 4) bands
#for loop to look for .tif file extenstions
for file in files:
    # filter to get the. tif files
    if file.lower().endswith('.tif'):
        if "_B40_" in file:
            # Set the Near-IR band
            band4 = file
        elif "_B30_" in file:
            # Set the Red Band
            band3 = file

try:
    # Open the raster files identified above
    band3 = gdal.Open(landsatFile + band3, gdalconst.GA_ReadOnly)
    band4 = gdal.Open(landsatFile + band4, gdalconst.GA_ReadOnly)
except:
    print("Unable to find or opn the needed bands to generate the NDVI band")
    exit()

# read the bands in as an array
b3 = band3.ReadAsArray()
b4 = band4.ReadAsArray()

# make the array's a float
b3 = 1.0 * b3
b4 = 1.0 * b4

# NDVI formula is (b4-b3)/(b4+b3)
# Complete the equation and output to a new array called ndvi
ndvi = (b4 - b3) / (b4 + b3)

try:
    # pull the driver data from one of the bands imported
    output = band3.GetDriver()  # copy input driver from the red band
    # get the columns and rows values from one layer
    columns = band3.RasterXSize
    rows = band3.RasterYSize
    # set number of bands output
    nBands = 1
    # set the datatype to a float
    dataType = gdalconst.GDT_Float32

    # Create the new raster layer
    outputNDVI = output.Create(landsatFile + "Final NDVI.TIF", columns, rows, nBands, dataType)

    # Set the GeoTransform from the same layer
    outputNDVI.SetGeoTransform(band3.GetGeoTransform())

    # Set the projection from the same layer
    outputNDVI.SetProjection(band3.GetProjection())

    # set the band we are going to write to.
    band1 = outputNDVI.GetRasterBand(1)

    # Push the data from the calculation above
    band1.WriteArray(ndvi)

    print("The Final NDVI.TIF file has been created.")

except:
    print("unable to write that file to the path ")
