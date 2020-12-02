#Python Program to Print All Permutations of a String in Lexicographic Order without Recursion
from math import factorial
def calculate_permutation(v):
    lst=list(v)
    c=0
    for i in range(factorial(len(lst))):
        print("".join(lst))
        m=len(lst)-1
        while lst[m-1]>lst[m]:
            m-=1
        lst[m:]=reversed(lst[m:])

        n=m
        while lst[m-1]>lst[n]:
            n+=1
        lst[m-1],lst[n]=lst[n],lst[m-1] #swaping
        c+=1
    print("Total=", c)

n=input("Enter a string:")
calculate_permutation(n)
