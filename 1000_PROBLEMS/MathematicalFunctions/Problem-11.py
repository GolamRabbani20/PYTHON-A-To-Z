#Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place
n=int(input("Enter a number:"))
m=n
count=0
while n>=1:
    count +=1
    n=n//10

s1=str(m)
s2=s1[count-1]
s3=str(count)

print("The new number formed:",int(s3+s2))