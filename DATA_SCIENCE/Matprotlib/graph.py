from matplotlib import pyplot as plt
x=[1,2,3]
y=[1,4,9]
z=[10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("Test plot")
plt.xlabel("X axis")
plt.ylabel("Y ans Z axis")
plt.legend(["This is Y","This is Z"])
plt.show()