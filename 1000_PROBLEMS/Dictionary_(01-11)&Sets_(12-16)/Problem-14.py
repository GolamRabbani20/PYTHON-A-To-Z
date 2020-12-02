#Python Program that Displays which Letters are in the First String but not in the Second
s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")
lst=list(set(s1)-set(s2))
for k in lst:
    print(k)