import geopandas as gpd
# Read in the data
full_data = gpd.read_file("../input/geospatial-learn-course-data/DEC_lands/DEC_lands/DEC_lands.shp")

# View the first five rows of the data
full_data.head()

# This dataset is provided in GeoPandas
world_filepath = gpd.datasets.get_path('naturalearth_lowres')
world = gpd.read_file(world_filepath)
world.head()

# Your code here
# Define a base map with county boundaries
ax = world.plot(figsize=(10,10), color='none', edgecolor='gainsboro', zorder=3)

# Add world loans to the base map
full_data.plot(color='lightgreen', ax=ax)

#Re-project to Mercator / EPSG32630
full_data.to_crs(epsg=32630)

# Change the CRS to EPSG 4326
full_data.to_crs("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs").head()

# Get the x-coordinate of each point
full_data.geometry.x.head()

# Calculate the area (in square meters) of each polygon in the GeoDataFrame 
world.loc[:, "AREA"] = world.geometry.area / 10**6

print("Area of Ghana: {} square kilometers".format(world.AREA.sum()))
print("CRS:", world.crs)
world.head()

# Set the coordinate reference system (CRS) to EPSG 4326
facilities.crs = {'init': 'epsg:4326'}

# GeoDataFrame showing path for each bird
path_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: LineString(x)).reset_index()
path_gdf = gpd.GeoDataFrame(path_df, geometry=path_df.geometry)
path_gdf.crs = {'init' :'epsg:4326'}

# GeoDataFrame showing starting point for each bird
start_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[0]).reset_index()
start_gdf = gpd.GeoDataFrame(start_df, geometry=start_df.geometry)
start_gdf.crs = {'init' :'epsg:4326'}

# Show first five rows of GeoDataFrame
start_gdf.head()

# Country boundaries in South America
south_america = americas.loc[americas['continent']=='South America']

#Calculate the total area of South America (in square kilometers)
totalArea = sum(south_america.to_crs(epsg=3035).area) / 10**6

P_Area = sum(protected_areas['REP_AREA']-protected_areas['REP_M_AREA'])
print("South America has {} square kilometers of protected areas.".format(P_Area))

# What percentage of South America is protected?
percentage_protected = P_Area/totalArea
print('Approximately {}% of South America is protected.'.format(round(percentage_protected*100, 2)))

