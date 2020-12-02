#Python Program that Displays which Letters are Present in Both the Strings
s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")
#a=set(s1)
#b=set(s2)
#lst=list(set(s1).union(set(s2)))
lst=list(set(s1)|set(s2))

for k in lst:
    print(k)

