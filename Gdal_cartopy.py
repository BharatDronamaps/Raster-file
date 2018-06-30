import os
import rasterio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

utm43n = ccrs.UTM(43)
ax = plt.axes(projection=utm43n)
plt.title('UTM zone 43N')

raster_file = 'Elevation_export.tif'

with rasterio.open(raster_file) as src:
    left, bottom, right, top = src.bounds
    ax.imshow(src.read(1), origin='upper',
              extent=(left, right, bottom, top), cmap='gray')
    x = [left, right, right, left, left]
    y = [bottom, bottom, top, top, bottom]
    ax.coastlines(resolution='10m', linewidth=4, color='red')
    ax.gridlines(linewidth=2, color='lightblue', alpha=0.5, linestyle='--')

plt.savefig('rasterio_cartopy.png', dpi=300)
plt.show()
