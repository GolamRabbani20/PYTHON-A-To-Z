import pandas as pd
df = pd.read_csv('NewYork_Weather.csv')
#print(df)

Max_temperature = df['Temperature'].max()
print("Max temperature =",Max_temperature)
print("List of days when it rained\n",df['EST'][df['Events']=='Rain'])

df.fillna(0, inplace=True)                      # Data Munging or Data Warning
Average_WindSpeed = df['WindSpeedMPH'].mean()
print("Average windSpeed = ",Average_WindSpeed)