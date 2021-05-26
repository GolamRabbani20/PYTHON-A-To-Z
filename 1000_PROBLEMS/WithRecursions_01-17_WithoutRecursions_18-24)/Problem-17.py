def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1::2]) + length(lst[2::2])

a=int(input("Enter size:"))
x=[]
for k in range(a):
    x.append(input("Enter element-"+str(k+1)+":"))
print("Length of the string is:",length(x))