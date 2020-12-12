#j kono word ar letter guli k koto vabe shagano jay?
from string import ascii_uppercase as k
def Pernutation(word):
    Result=1
    for letter in set(k):
        n=word.upper().count(letter.upper())
        if n>1:
           Result*=Factorial(n)
    return Factorial(len(word))//Result

def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)

print(Pernutation(input("Enter a word:")))