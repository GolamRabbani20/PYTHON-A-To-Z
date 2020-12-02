def EqualizeTheArray(x):
       temp=[0]*(max(x)+1)
       for k in x:
           temp[k]+=1
       return len(x)-max(temp)

input()
x=list(map(int,input().split()))
print(EqualizeTheArray(x))