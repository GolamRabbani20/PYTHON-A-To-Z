n=[2,6,7,9,11,12]

#Map comprehensive
result=[x*x for x in n]
print(result)

#filter comprehensive
r=[x for x in n if x%2==0]
print(r)

p=[x for x in n if x%2==1]
print(p)