import pandas as pd
import folium
from folium.plugins import HeatMap

coords = pd.read_csv("library_coords.csv")  # has Library, Latitude, Longitude

# visits data
path = "..."
df = pd.read_excel(path, sheet_name="...", skiprows=2)
df.columns = df.columns.str.strip()
visits = df[["Location", "Library Visits"]]

# library name merge
merged = pd.merge(coords, visits, left_on="Library", right_on="Location", how="inner")
merged = merged.dropna(subset=["Latitude", "Longitude", "Library Visits"])

# folium map
m = folium.Map(location=[44.3, -85.6], zoom_start=6)

# create weighted points: [lat, lon, visits]
heat_data = merged[["Latitude", "Longitude", "Library Visits"]].values.tolist()

# heatmap
HeatMap(heat_data, radius=15, blur=10, max_zoom=10).add_to(m)

# save to HTML
m.save("michigan_library_visits_heatmap.html")
print("✅ Map saved to michigan_library_visits_heatmap.html")
