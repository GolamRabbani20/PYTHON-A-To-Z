x=[]
for i in range(int(input("Enter number of nodes:"))):
    data=input("Enter data:")
    x.append(data.upper())

while True:
    n=int(input("Enter position:"))
    L=(2*n)+1
    R=(2*n)+2
    P=(n-1)//2

    if L>len(x) or L<0:
        print(x[n]+" has no left child")
    else:
       print("Left child of"+x[n]+" is:",x[L])

    if R> len(x) or R <0:
        print(x[n]+" has no Right child")
    else:
        print("Right child of"+x[n]+" is:",x[R])

    print("Parent of "+x[n]+" is:",x[P])