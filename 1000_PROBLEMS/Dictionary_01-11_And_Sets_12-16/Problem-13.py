#Python Program to Check Common Letters in Two Input Strings
s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")

lst=list(set(s1)&set(s2))
for k in lst:
    print(k)

''''
for i in s1:
    for k in s2:
        if i==k:
            print(i)
'''