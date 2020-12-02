import numpy as np

x=np.array([10,20,30,40])
y=np.array([4,5,6,7])
new=np.add(x,y)
print("Add=",new)

new1=np.subtract(x,y)
print("Sub=",new1)

new2=np.multiply(x,y)
print("Multi=",new2)

new3=np.divide(x,y)
print("Division=",new3)

new4=np.mod(x,y)
print("Remainder=",new4)

new5=np.remainder(x,y)
print("Remainder1=",new5)

Quotient_Mod=np.divmod(x,y)
print("Quotient and Mod=",Quotient_Mod)

k=np.array([-1,5,-10,12,-45,-25])
h=np.absolute(k)
print("AbsoluteValue=",h)