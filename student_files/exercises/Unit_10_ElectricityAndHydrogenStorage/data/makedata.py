import geokit as gk
from smopy import deg2num
import reskit as rk

shapeFilePath = "/storage/internal/data/c-winkler/04_Data/02_Geodata_processed/Political_Geography/gadm_per_gid_0_east_west_plus_area_split/global/gadm36_GID1(0)_EastWest_and_largeRegion_split_epsg4326_withUnion.shp"
shape = gk.vector.extractFeatures(shapeFilePath)
shape_NER = shape[shape.GID_0 == "NER"]
shape_NER["centroid"] = shape_NER["geom"].apply(lambda g:g.Centroid())
shape_NER["country"] = shape_NER["geom"]
shape_NER["lon"] = shape_NER["centroid"].apply(lambda g:g.GetX())
shape_NER["lat"] = shape_NER["centroid"].apply(lambda g:g.GetY())

def get_tile(xy):
    x = xy[0]
    y = xy[1]
    tile = f"/storage/internal/data/gears/weather/ERA5/processed/4/{x}/{y}/2015/"
    return tile
shape_NER["era5_path"] = shape_NER[["lon", "lat"]].apply(lambda x: get_tile(deg2num(x.lon, x.lat, 4)), axis=1)

shape_NER = gk.vector.extractFeatures(gk.vector.mutateVector(gk.vector.createVector(shape_NER), srs=2931))
shape_NER["area"] = shape_NER["geom"].apply(lambda g:g.Area()*0.1)
shape_NER["capacity"] = shape_NER["area"]/20
pass
out_solar = rk.solar.openfield_pv_era5(
    placements=shape_NER.drop(columns=["geom"]),
    era5_path=shape_NER["era5_path"].iloc[0],
    global_solar_atlas_dni_path="/storage/internal/data/gears/geography/irradiance/global_solar_atlas_v2.5/World_DNI_GISdata_LTAy_AvgDailyTotals_GlobalSolarAtlas-v2_GEOTIFF/DNI.tif",
    global_solar_atlas_ghi_path="/storage/internal/data/gears/geography/irradiance/global_solar_atlas_v2.5/World_GHI_GISdata_LTAy_AvgDailyTotals_GlobalSolarAtlas-v2_GEOTIFF/GHI.tif",
)


cfs = out_solar.capacity_factor.to_dataframe().unstack('location').fillna(0)
cfs.columns = shape_NER.GID_1
cfs.to_csv("/storage/internal/home/d-franzmann/code/modelBuilder/test/spatial_data/solar_ts_NER.csv")

caps = out_solar.capacity.to_series().to_frame().T
caps.columns = shape_NER.GID_1
caps.to_csv("/storage/internal/home/d-franzmann/code/modelBuilder/test/spatial_data/solar_cap_NER.csv")


shape_NER["hub_height"] = 130
shape_NER["rotor_diam"] = 100

out_wind = rk.wind.onshore_wind_era5(
    placements=shape_NER.drop(columns=["geom"]),
    era5_path=shape_NER["era5_path"].iloc[0],
    gwa_100m_path="/storage/internal/data/gears/geography/wind/global_wind_atlas/GWA_3.0/gwa3_250_wind-speed_100m.tif",
    esa_cci_path="/storage/internal/data/gears/geography/landcover/esa_cci_v2.1.1/C3S-LC-L4-LCCS-Map-300m-P1Y-2018-v2.1.1.tif",
)
cfs = out_solar.capacity_factor.to_dataframe().unstack('location').fillna(0)
cfs.columns = shape_NER.GID_1
cfs.to_csv("/storage/internal/home/d-franzmann/code/modelBuilder/test/spatial_data/onshore_ts_NER.csv")

caps = out_solar.capacity.to_series().to_frame().T * (shape_NER.area / 1E8)
caps.columns = shape_NER.GID_1
caps.to_csv("/storage/internal/home/d-franzmann/code/modelBuilder/test/spatial_data/onshore_cap_NER.csv")

