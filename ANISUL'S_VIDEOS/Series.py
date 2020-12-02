n=int(input("Enter a number: "))
sum=1

"""
#1+2+3+......+n; Summation of 1 to n.

for i in range(1,n+1):
    sum=sum+i
print(sum)

#2+4+6+......+n; Summation of all even number from 2 to n.

for i in range(2,n+1,2):
    sum=sum+i
print(sum)

#1+3+6+9+12+........+n=sum
for i in range(1,n+1,3):
    sum=sum+i
print(sum)

#1*3*6*9*12*........*n=sum
sum=1
for i in range(1,n+1,3):
    sum=sum*i
print(sum)

#1*2+2*2+3*2+4*2+..............+n+n=sum
for i in range(1,n+1):
    sum=sum+i*i
print(sum)
"""
#1*1*2*2*3*3*.....*n*n=sum
for i in range(1,n+1,1):
    sum=sum*i*i
print(sum)