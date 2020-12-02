#Python Program to Find all Numbers in a Range which are Perfect Squares and Sum
#of all Digits in the Number is Less than 10

m=int(input("Enter lower range:"))
n=int(input("Enter upper range:"))
x=[x for x in range(m,n+1) if (int(x**0.5)**2==x) and sum(list(map(int,str(x))))<10]
print(x)

'''
x=[]
for i in range(m,n+1):
    if int(i**0.5)**2==i and sum(list(map(int,str(i))))<10:
      x.append(i)
print(x)
'''
