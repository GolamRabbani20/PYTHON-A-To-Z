#Python Program to Convert Gray Code to Binary
def gray_to_bin(n):
    x=int(n,2)
    m=x
    while m>0:
        m=m>>1
        x=x^m
    return bin(x)
g=input("Enter a gray code:")
s=gray_to_bin(g)
print("In binary:",s[2:]) #[2:]  remove the "0b"
