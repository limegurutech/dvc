import pandas as pd
import yaml
import os 
import io

params = yaml.safe_load(open("params.yaml"))['filter']
df = pd.read_csv("weather-data/2006-04-10.csv", parse_dates=["Formatted Date"])
df = df[df['Temperature (C)'] > params['value']]
df = df[['Formatted Date', 'Temperature (C)']]
print(df)
os.makedirs(os.path.join("output", "filter"), exist_ok=True)
df.to_csv("output/filter/out.csv")
