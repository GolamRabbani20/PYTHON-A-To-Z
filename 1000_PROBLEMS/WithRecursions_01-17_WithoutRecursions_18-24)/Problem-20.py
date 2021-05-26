#Python Program to Flatten a List without using Recursion
a=[[1,[[2]],[[[3]]]],[[4],5]]
flatten=lambda k: sum(map(flatten,k),[]) if isinstance(k,list) else [k]
print(flatten(a))
