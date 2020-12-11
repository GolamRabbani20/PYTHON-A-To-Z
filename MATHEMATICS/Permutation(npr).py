def Permutation(n,r):
    if n==r:
        return Factorial(n)
    else:
     return Factorial(n)//Factorial(n-r)

def Combination(n,r):
    if n==r:
        return 1
    else:
      return Factorial(n)//(Factorial(r)*Factorial(n-r))

def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)

n,r=input().split()
n,r=[int(n),int(r)]
print("Result =",Permutation(n,r))
print("Combination =",Combination(n,r))