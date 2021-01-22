import pandas as pd
weather_data={  #Create DataFrame Using Dictonary
    'Day':['20/01/21', '21/01/21', '22/01/21', '23/01/21', '24/01/21', '25/01/21', '26/01/21', '27/01/21'],
    'Temperature': [32, 35, 25, 26, 45, 20, 12, 22],
    'Windspeed':[6,7,8,10,9,5,4,6],
    'Event': ['Rain', 'Sunny', 'Rain', 'Snow', 'Snow', 'Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print(df)

print("\n..................................................Create DataFrame Using CSV")
df2 = pd.read_csv('Test02.csv')
print(df2)

print("\n.................................................................")
print(df[["Day","Event","Temperature"]])

print("\n.................................................................Event")
print(df.Event)