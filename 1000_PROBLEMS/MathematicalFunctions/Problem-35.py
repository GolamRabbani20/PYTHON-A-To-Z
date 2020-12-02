#Python Program to Count Set Bits in a Number
def count_set_bit(n):
    count=0
    while n>1:
        n &= n-1     #n=5=>101&100=100=4=n count=1;n=4=>100&011=000=n count=2 as 0>1 false print
        count=count+1
    return count
n=int(input("Enter the value of n:"))
print("result=",count_set_bit(n))