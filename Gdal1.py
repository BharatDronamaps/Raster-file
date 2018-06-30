import os
import matplotlib.pyplot as plt
from osgeo import gdal

# GDAL does not use python exceptions by default
gdal.UseExceptions()

raster_file = 'Orthomosaic_export.tif'

geo = gdal.Open(raster_file)
drv = geo.GetDriver()
print(drv.GetMetadataItem('DMD_LONGNAME'))
img = geo.ReadAsArray()
print(img.shape)

plt.imshow(img[0,:,:], cmap='gray')
plt.show()
