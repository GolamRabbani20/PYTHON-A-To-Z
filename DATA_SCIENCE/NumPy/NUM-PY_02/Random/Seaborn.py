import matplotlib.pyplot as plt
import seaborn as sb

sb.distplot([0, 1, 2, 3, 4, 5])
plt.show()

sb.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()