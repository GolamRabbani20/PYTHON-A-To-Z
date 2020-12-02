#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
n=input("Enter a string:")
lst=n.split()
d={}
for x in lst:
    if x[0] not in d.keys():
        d[x[0]]=[]
        d[x[0]].append(x)
    else:
        if x not in d[x[0]]:
            d[x[0]].append(x)
for k,v in d.items():
    print(k,":",v)