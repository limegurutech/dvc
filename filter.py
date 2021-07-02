import pandas as pd
import yaml

params = yaml.safe_load(open("params.yaml"))['filter']
df = pd.read_csv("weather-data/2006-04-10.csv", parse_dates=["Formatted Date"])
rslt_df = df[df['Temperature (C)'] > params['value']]
print(">>")
print(rslt_df)
