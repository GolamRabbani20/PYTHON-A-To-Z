x=[1,4,5,2,5,6,25,45,100]
n=int(input("Enter a value:"))
flag=0

"""
for k in range(len(x)):
    if x[k]==n:
        print(n,"is fount at position-",k+1)
        flag=1
        break
if flag==0:
    print(n,"is not present in the list")   
    
"""

for k in x:
    if k==n:
        print(n,"is fount at position-",x.index(k)+1)
        flag=1
        break
if flag==0:
    print(n,"is not present in the list")