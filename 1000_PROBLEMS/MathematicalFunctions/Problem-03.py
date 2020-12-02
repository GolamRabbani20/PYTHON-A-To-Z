#Python Program to Check Whether a Given Year is a Leap Year
a=int(input("Enter a year as (Lower Range):"))
b=int(input("Enter a year as (Lower Range):"))

leap=[]
not_leap=[]

for x in range(a,b+1):

     if (x%4==0 and x%100!=0 or x%400==0):
         leap.append(x)
         #print(x,"is a leap year.")
     else:
        #print(x,"is not a leap year.")
        not_leap.append(x)

print("List of leap year:",leap)
print("List of non leap year:",not_leap)