import pandas as pd

path = "..."
df = pd.read_excel(path, sheet_name="...")

df.columns = df.columns.str.strip()
df["columnHeader"] = df["columnHeader"].astype(str)
df["columnHeader"] = df["columnHeader"].str.strip()

libraries = df["columnHeader"].dropna().unique().tolist()

queries = [f"{lib}, Michigan" for lib in libraries]

# get a clean list of unique library names
names = (
    df["columnHeader"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
    .tolist()
)

print(len(names), "libraries")
print(names[:390])
