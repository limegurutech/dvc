import pandas as pd
import yaml

params = yaml.safe_load(open("params.yaml"))['training']
df = pd.read_csv("weather-data/2006-04-10.csv", parse_dates=["Formatted Date"])
df = df.head(params['num_rows'])
mean = df['Temperature (C)'].mean()
print(mean)



