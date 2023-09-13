# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:54:07 2020

@author: Sunday
"""

#ncfile

from netCDF4 import Dataset
import numpy as np
from osgeo import gdal
from osgeo import gdal_array
from osgeo import osr
import matplotlib.pylab as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature


nc_file = 'D:\\image\\process\\roll56D0\\reanalysis data1000hpa.nc'
fh = Dataset(nc_file, mode='r')
lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
vw = fh.variables['w'][0,:,:]
u = fh.variables['u'][0,:,:]
v = fh.variables['v'][0,:,:]
t = fh.variables['t'][0,:,:]

vs = np.sqrt(u**2+v**2)

Lon, Lat = np.meshgrid(lons, lats)


fig = plt.figure(figsize=(25,25))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-160, -145, 62, 52], crs=ccrs.PlateCarree())
#ax.pcolormesh(Lon,Lat,vs,cmap='plasma',transform=ccrs.PlateCarree())
ax.pcolormesh(Lon,Lat,t,cmap='plasma',transform=ccrs.PlateCarree())



ax.barbs(Lon[::3,::3],Lat[::3,::3], u[::3,::3], v[::3,::3], length=5,
         sizes=dict(spacing=0.2, height=0.5),
         linewidth=0.95, transform=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE.with_scale('10m'))
#im = ax.imshow(vs, transform=ccrs.PlateCarree(), cmap='plasma')
im = ax.imshow(t, transform=ccrs.PlateCarree(), cmap='plasma')
plt.colorbar(im, fraction=0.018, pad=0.04).set_label(label="Temperature [K]",size=15)
#plt.colorbar(im, fraction=0.018, pad=0.04).set_label(label="wind speed [m/s]",size=15)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')

#gl.xlocator = mticker.FixedLocator([-156, -155, -154, -153, -152 , -151, -150])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 15, 'color': 'gray'}
gl.xlabel_style = {'color': 'red', 'weight': 'bold'}


plt.show()
