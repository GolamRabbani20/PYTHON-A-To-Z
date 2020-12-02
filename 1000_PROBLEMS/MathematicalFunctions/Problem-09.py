#Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
n=int(input("Enter the size of list:"))
s=[]
pEven=0
pOdd=0
nNum=0
for i in range(1,n+1):
    s.append(int(input("Enter element:")))

for k in s:
    if k%2==0 and k>0:
        pEven+=k
    elif k>0 and k%2==1:
        pOdd += k
    else:
        nNum += k

print("Sum of negative number:",nNum)
print("Sum of Positive Even number:",pEven)
print("Sum of Positive Odd number:",pOdd)