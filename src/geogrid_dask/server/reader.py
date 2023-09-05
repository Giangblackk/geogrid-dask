import rioxarray
from rio_tiler.io import XarrayReader


# open dataset with rioxarray
xds = rioxarray.open_rasterio("datasets/HYP_50M_SR.cog.tif")

# create xarray reader for xarray data
dst = XarrayReader(xds)

# get tile 2/2/2 in TMS
tile_2_2_2 = dst.tile(tile_x=2, tile_y=2, tile_z=2)

# render image to buffer of image in GeoTiff format
img = tile_2_2_2.render(img_format="GTiff")

# save rendered image
with open("datasets/HYP_50M_SR_2_2_2.tif", "wb") as f:
    f.write(img)
