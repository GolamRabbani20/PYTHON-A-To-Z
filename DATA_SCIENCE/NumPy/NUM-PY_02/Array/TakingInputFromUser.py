from array import *

arr = array('i',[])
n = int(input("Enter array size:"))
for i in range(n):
    arr.append(int(input("Enter a value:")))
for k in arr:
    print(k, end=" ")
print()


arr2 = array('i', [])
for i in list(map(int,input().split())):
    arr2.append(i)
for k in arr2:
    print(k,end=" ")

