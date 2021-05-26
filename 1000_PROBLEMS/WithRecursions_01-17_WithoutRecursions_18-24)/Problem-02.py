#Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
def counts(s,n):
    if not s:       # s is empty or not
        return 0
    elif s[0]==n:
        return 1+counts(s[1:],n)
    else:
        return counts(s[1:],n)

x=input("Enter a string:")
n=input("Enter a letter:")
print(counts(x,n))