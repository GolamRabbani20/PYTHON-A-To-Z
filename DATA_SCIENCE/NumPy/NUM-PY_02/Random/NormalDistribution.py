from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb

x = random.normal(size=(2, 3))
print(x)

print("\n.............................................")
m = random.normal(loc=1, scale=2, size=(2, 3))
print(m)

sb.distplot(random.normal(size=1000), hist=False)
plt.show()