#Python Program to Clear the Rightmost Set Bit of a Number
def clear_rightmost_setbit(n):
    return n & (n-1)
n=int(input("Enter a number:"))
print("n with its rightmost set bit cleared equals:",clear_rightmost_setbit(n))