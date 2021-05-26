#Python Program to Find the Sum of Elements in a List Recursively
def sumoflist(lst,size):
      if size==0:
          return 0
      else:
          return lst[size-1]+sumoflist(lst,size-1)

n=int(input("Enter size:"))
lst=[]
for k in range(n):
    lst.append(int(input("Enter element:")))

print("Sum of the elements:",sumoflist(lst,n))
