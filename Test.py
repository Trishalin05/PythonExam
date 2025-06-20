import pandas as pd

url = "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_station_data.csv"
df = pd.read_csv(url)

print(df.head())