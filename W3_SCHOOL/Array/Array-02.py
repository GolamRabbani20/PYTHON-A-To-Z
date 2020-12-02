import  array as arr
arr=arr.array('i',[])
n=int(input("Enter size:"))
for i in range(n):
    arr.append(int(input("Enter element:")))

for i in range(n):
    print("In index",arr.index(arr[i]),"=",arr[i])
flag=0
x=int(input("Enter item:"))
p=0
for k in arr:
    if k==x:
        print(k,"is present in the position",arr.index(k)+1)
        print("index=",p)
        flag=1
        break
    p+=1
if flag==0:
   print(x,"is not present in array.")