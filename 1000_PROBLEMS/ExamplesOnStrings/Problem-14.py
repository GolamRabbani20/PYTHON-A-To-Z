#Python Program to Check if a String is a Pangram or Not
'''
Pangram means the string has every letter at lest once
Ex: The quick brown fox jumps over the lazy dog
'''
from string import ascii_lowercase as x
#print(x)
#print(set(x)-{'a','b','d'})
def check(n):
    return set(x)-set(n.lower())==set([])

string=input("Enter a string:")

if (check(string)==1):
    print("The String is a Pangram")
else:
    print("The String is not a Pangram")



