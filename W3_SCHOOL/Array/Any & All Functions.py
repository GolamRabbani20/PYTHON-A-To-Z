'''
**Any and All are two built-in function  provided in python used for successive And/Or.
Any:It Returns true if any of the items is True. It returns False if empty or all are false
All: Returns true if all of the items are True (or if the iterable is empty) other wise False
'''

x=[10,41,81,121,401]
m=[]

print(any(n%2==0 for n in x))

k=[1,3,5]

print(all(n%2==0 for n in k))
print(all(n%2==0 for n in x))
p=[]
print(all(p))