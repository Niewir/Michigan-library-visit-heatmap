import pandas as pd, geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as cx

# load + merge
coords = pd.read_csv("library_coords.csv")  # Library, Latitude, Longitude
xl = "..."
vis = pd.read_excel(xl, sheet_name="...", skiprows=2)[["Location", "Library Visits"]]

df = coords.merge(vis, left_on="Library", right_on="Location", how="inner").dropna(subset=["Latitude","Longitude"])
df["Library Visits"] = pd.to_numeric(df["Library Visits"], errors="coerce")

# GeoDataFrame in Web Mercator for tiles
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
    crs="EPSG:4326"
).to_crs("EPSG:3857")

# scale sizes with outlier clipping (10th–90th pct)
v = gdf["Library Visits"].clip(gdf["Library Visits"].quantile(0.1),
                               gdf["Library Visits"].quantile(0.9))
sizes = (v - v.min())/(v.max()-v.min()+1e-9) * 200 + 20  # 20..220

# plot
fig, ax = plt.subplots(figsize=(8,10), dpi=150)
gdf.plot(ax=ax, column="Library Visits", cmap="viridis",
         markersize=sizes, alpha=0.85, edgecolor="white", linewidth=0.2,
         legend=True, legend_kwds={"label": "Library Visits"})

# use a supported basemap (Stamen is deprecated)
cx.add_basemap(ax, source=cx.providers.CartoDB.Positron, attribution_size=6)

ax.set_axis_off()
plt.title("Michigan Library Visits")
plt.tight_layout()
plt.savefig("michigan_library_visits.png", bbox_inches="tight")
print("Saved michigan_library_visits.png")
