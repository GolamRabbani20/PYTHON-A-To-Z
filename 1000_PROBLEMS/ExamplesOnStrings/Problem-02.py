#Python Program to Remove the nth Index Character from a Non-Empty String
def remove(x,n):
    first=x[:n]
    last=x[n+1:]
    return first+last

x=input("Enter string:")
n=int(input("Enter index number:"))
print("New String is:",remove(x,n))