import pandas as pd


df = pd.read_csv("../datasets/TVShows.csv")
print(df)

df.dropna(inplace=True)
print(df)

df.drop_duplicates(inplace=True)
print(df)

df = df.drop(["S","E"], axis = 1)
print(df)

df.rename(columns={"tconst":"id"},inplace=True)
print(df)

df['averageRating'] = pd.to_numeric(df['averageRating'],errors="coerce")
df=df.dropna(subset=["averageRating"]).astype({"averageRating":"float"})
print(df["averageRating"])

df['year'] = pd.to_numeric(df['year'],errors="coerce")
df=df.dropna(subset=["year"]).astype({"year":"int"})
print(df["year"])

df['minutes'] = pd.to_numeric(df['minutes'],errors="coerce")
df=df.dropna(subset=["minutes"]).astype({"minutes":"int"})
print(df["minutes"])

for x in df.index:
  if df.loc[x, "year"] > 2020:
    df.loc[x, "year"] = 2020
  elif df.loc[x,"year"]<1950:
    df.loc[x,"year"]=1950
print(df)


df = df.to_csv("../datasets/TVShows_new.csv")

df = pd.read_csv("../datasets/TVShows.csv")
df