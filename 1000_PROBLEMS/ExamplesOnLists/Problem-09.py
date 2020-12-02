#Python Program to Find the Intersection of Two Lists
def intersection(x,y):
    return list(set(x) & set(y))

def mango():
    x = []
    y = []
    n = int(input("Enter list size1:"))
    for i in range(n):
        x.append(int(input("Enter Element list1:")))

    m = int(input("Enter list size2:"))
    for k in range(m):
        y.append(int(input("Enter Element for list2:")))

    print("The intersection of two list:",intersection(x,y))
mango()
