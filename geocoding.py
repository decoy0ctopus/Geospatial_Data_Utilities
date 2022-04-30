import geopandas
from geopandas.tools import geocode

result = geocode("The Great Pyramid of Giza", provider="nominatim")
print(result)

point = result.geometry.iloc[0]
print("Latitude:", point.y)
print("Longitude:", point.x)

#Download list of universities

universities = pd.read_csv("../input/geospatial-learn-course-data/top_universities.csv")
universities.head()

def my_geocoder(row):
    try:
        point = geocode(row, provider='nominatim').geometry.iloc[0]
        return pd.Series({'Latitude': point.y, 'Longitude': point.x, 'geometry': point})
    except:
        return None

universities[['Latitude', 'Longitude', 'geometry']] = universities.apply(lambda x: my_geocoder(x['Name']), axis=1)

print("{}% of addresses were geocoded!".format(
    (1 - sum(np.isnan(universities["Latitude"])) / len(universities)) * 100))

# Drop universities that were not successfully geocoded
universities = universities.loc[~np.isnan(universities["Latitude"])]
universities = gpd.GeoDataFrame(universities, geometry=universities.geometry)
universities.crs = {'init': 'epsg:4326'}
universities.head()

# Create a map
m = folium.Map(location=[54, 15], tiles='openstreetmap', zoom_start=2)

# Add points to the map
for idx, row in universities.iterrows():
    Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)

# Use an attribute join to merge data about countries in Europe
europe = europe_boundaries.merge(europe_stats, on="name")
europe.head()

# Use spatial join to match universities to countries in Europe
european_universities = gpd.sjoin(universities, europe)

# Investigate the result
print("We located {} universities.".format(len(universities)))
print("Only {} of the universities were located in Europe (in {} different countries).".format(
    len(european_universities), len(european_universities.name.unique())))

european_universities.head()

#The spatial join above looks at the "geometry" columns in both GeoDataFrames. 
#If a Point object from the universities GeoDataFrame intersects a Polygon object from the europe DataFrame, the corresponding rows are combined and added as a single row of the european_universities DataFrame. 
#Otherwise, countries without a matching university (and universities without a matching country) are omitted from the results.

# Select counties with certain values
sel_counties = CA_stats[((CA_stats.high_earners > 100000) &
                         (CA_stats.median_age < 38.5) &
                         (CA_stats.density > 285) &
                         ((CA_stats.median_age < 35.5) |
                         (CA_stats.density > 1400) |
                         (CA_stats.high_earners > 500000)))]

sel_counties.head()

# Check your answer
q_4.check()