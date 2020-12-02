x=[1,2,5,4,6,8,6,10,15]

def Is_even(x):
    return x%2==0

even=filter(Is_even,x)  # x is an iterable object that work as loop
for p in even:
   print(p,end=" ")
print()
odd=list(filter(lambda k:k%2==1,x))
print(odd)

n=[1,5,85,9,36,98,96,45,996,6,99,93,70,50,6,10]
def FindAbove20(k):
    #return k>20
    if k<20:
        return False
    else:
        return True

numbers=filter(FindAbove20,n)
num=list(filter(lambda w:w<50,n))
print(num)

for i in numbers:
    print(i,end=" ")