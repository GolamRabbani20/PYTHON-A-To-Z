#Python Program to Find the Gravitational Force Acting Between Two Objects
m1=float(input("Enter mass of m1:"))
m2=float(input("Enter mass of m2:"))
r=float(input("Enter distance between m1 & m2:"))
G=6.673*(10**-11)
F=(m1*m2*G)/(r**2)
print("The Gravitational Force:",round(F,3),"N")