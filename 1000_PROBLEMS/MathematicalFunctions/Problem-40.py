#Python Program to Convert Binary to Gray Code
def bin_to_gray(n):
    #n=int(n,2)
    n^=(n>>1)
    return bin(n)
n=int(input("Enter a binary number:"),2)
g=bin_to_gray(n)
print("In gray:",g[2:])
print("The equivalent value of gray codes:",int(g[2:],2))
