#Python Program that Displays which Letters are in the Two Strings but not in Both
s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")
lst=list(set(s1)^set(s2))
for i in lst:
    print(i)