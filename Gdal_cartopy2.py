import os
import rasterio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

utm43n = ccrs.UTM(43)
merc = ccrs.Mercator()
ax = plt.axes(projection=merc)

raster_file = 'Orthomosaic_export.tif'

with rasterio.open(raster_file) as src:
    left, bottom, right, top = src.bounds
    ax.set_extent((left, right, bottom, top), utm43n)
    ax.imshow(src.read(1), origin='upper', transform=utm43n,
              extent=(left, right, bottom, top), cmap='gray',
              interpolation='nearest')
    x = [left, right, right, left, left]
    y = [bottom, bottom, top, top, bottom]
    ax.coastlines(resolution='10m', linewidth=4, color='red')
    ax.gridlines(linewidth=2, color='lightblue', alpha=0.5, linestyle='--')

plt.savefig('rasterio_cartopy2.png', dpi=300)
plt.show()
