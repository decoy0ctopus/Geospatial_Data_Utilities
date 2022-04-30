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