#Python Program to Find the Cumulative Sum of a List where the ith Element
# is the Sum of the First i+1 Elements From The Original List
n=int(input("Enter number of elements:"))
x=[]
for i in range(n):
    x.append(int(input("Enter element:")))
print("Original list is:",x)

a=[sum(x[0:k+1]) for k in range(0,len(x))]
print("The new list is:",a)

'''
y=[]
s=0
for k in range(n):
    if k==0:
        s=s+x[0]
        y.append(s)
    elif k>=1:
        s=s+x[k]
        y.append(s)
print("New list:",y)
'''


