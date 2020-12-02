def Binary_Search(x,data):
    left = 0
    right = len(x)-1
    while left<=right:
        mid = (left + right) // 2
        if x[mid]==data:
            return mid
            #print(data,"is found at position",x.index(data)+1)
        elif data>x[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1

x=[62,7,100,5,10,16,2,25,27,3,29,30,35,41,47,60]
x.sort()
print(x)
n=int(input("Enter search item:"))
k=Binary_Search(x,n)

if k>-1:
   print(n, "is found at position", k+1)
else:
    print(n, "is not found")