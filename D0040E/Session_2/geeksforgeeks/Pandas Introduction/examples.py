import pandas as pd

df = pd.read_csv("Session_2/geeksforgeeks/Pandas Introduction/music.csv",
    dtype={
        "listen_id": "int32",
        "source": "category",
        "artist": "string",
        "album": "string",
        "rating": "int8",
        "rating_label": "category",
        "supergenre": "category",
        "genre": "category",
        "subgenre": "category",
        "notes": "string"
    },
    parse_dates=["date", "release_date"])

df['release_date'] = df['release_date'].dt.to_period('M')

print("Max number of rows to display:", pd.options.display.max_rows) 

print(df.describe())

print(df.info())

print(df.isnull().sum())
df = df.fillna(0)

release = df[df['release_date'] == '2019-04']
print(release)

very_good = df[df['rating'] == 2]
print(very_good)

ser = pd.Series(df['artist'])
data = ser.head(10)
print(data)

print(df.to_string())