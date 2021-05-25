import pandas as pd
from matplotlib import pyplot as plt

sample_data=pd.read_csv('sample_data.csv')
print(sample_data)
#print(type(sample_data))

print("\nAll data of column-'A'")
print(sample_data.column_a)
#print(type(sample_data.column_a))
#print('\n\n')
#print(sample_data.iloc[3])
#print(sample_data.column_c.iloc[2])

plt.title("Test1")
plt.plot(sample_data.column_a,sample_data.column_b,'o')  #'o' is used for matplotlib's offical documentation
plt.plot(sample_data.column_a,sample_data.column_c)

plt.xlabel("Column-a")
plt.ylabel("Column-b and Column-c")
plt.legend(["This is column-b","This is column-c"])

plt.show()