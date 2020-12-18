import numpy as np
arr = np.array([1, 2, 3, 4, 8])
for i in arr:
    print(i,end=" ")
print()

x = np.array([[1,2,3,4], [5,6,7,8]])
for k in x:
    print(x)

arr1 = np.array([[1,2,3],[4,5,6]])
for i in arr1:
    for k in i:
        print(k,end=" ")
print()

for h in arr1[0:,0:]:
    for j in h:
        print(j,end=" ")

print("\n3DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
arr2 = np.array([[[1,2,3],[4,5,6]],[[1,5,9],[10,12,13]]])
for i in arr2:
    for k in i:
        for l in k:
            print(l,end=" ")

print("\n4444DDDDDDDDDDDDDDDDDDDDDDDD")

arr3 = np.array([[[[1,2,3],[2,3,4]],[[3,6,9],[2,5,8]]], [[[1,5,9],[1,7,0]],[[7,8,9],[1,7,3]]]])
print("Dimension =",arr3.ndim)
for a in arr3:
    for b in a:
        for c in b:
            for d in c:
                print(d,end=" ")

print("\n.................................................")
arr4 = np.array([[[[1,2,3],[2,3,4]],[[3,6,9],[2,5,8]]], [[[1,5,9],[1,7,0]],[[7,8,9],[1,7,3]]]])
for x in np.nditer(arr4):
    print(x,end=" ")


print("\n...................................................")
arr5 = np.array([0,2,35,5,6,7])
for k in  np.nditer(arr5, flags=['buffered'],op_dtypes=['S']):
    print(k,end=" ")

print("\n...................................................")
arr6 = np.array([[1,3,7,11],[10,12,15,20]])
for k in arr6[:,: :2]:
    for i in k:
        print(i,end=" ")

print("\n...................................................")
arr7 = np.array([[1,2,3],[10,40,90]])
for ind,k in np.ndenumerate(arr7):
    print(ind,k)

print("\n...................................................")
#d = int(input("Enter dimension:"))
#m = np.array(map(int,input().strip().split()),ndmin=2)
#m = m.reshape(2,3)
m = np.array([[1,2,3],[2,5,8]])
n = np.array([[1,5,9],[3,5,7]])

p = m[0:,: :]+n[0:,: :]
for k in p:
    for i in k:
        print(i,end=" ")
    print()