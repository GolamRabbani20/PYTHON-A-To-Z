import pandas as pd
from matplotlib import pyplot as plt

country_data=pd.read_csv('countries.csv')
#print(country_data)

#Af=country_data=="Afghanistan"      #Afghanistan true , All other countries is false
#print(Af)
#c=input("Enter country:")
for c in ["China","India","Bangladesh","Pakistan"]:
    bd=country_data[country_data.country==c]
    china=country_data[country_data.country=='China']
#print(bd)

    plt.title(c+" Vs China")
    plt.plot(bd.year,bd.population / 10**6,china.year,china.population/10**6)

    plt.xlabel("Years")
    plt.ylabel("Populations")

    plt.legend(['China',c])
    plt.show()


