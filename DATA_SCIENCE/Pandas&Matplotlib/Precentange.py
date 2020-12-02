import pandas as pd
from matplotlib import pyplot as plt

country_data=pd.read_csv('countries.csv')

c1=input("Enter country1:")
c2=input("Enter country2:")

x=country_data[country_data.country==c1]
y=country_data[country_data.country==c2]

plt.title(c1+" Vs "+c2+"")
plt.plot(x.year,x.population/x.population.iloc[0]*100,y.year,y.population/y.population.iloc[0]*100)

plt.xlabel("Years")
plt.ylabel("Population growth (First year = 100")

plt.legend([c2,c1])
plt.show()


