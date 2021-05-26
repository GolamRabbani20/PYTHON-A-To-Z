"""
# 10 50 60 20
x=input("Enter a number like test:")
m=x.split() # 10,50,60,20
sum=0
for n in m:
    sum=sum+int(n)
print(sum)
"""
n=input("Enter a text with number: ")
words=0
chars=0
digits=0
for x in n:
    x=x.lower()
    if x>='a' and x<='z': #or x>='A' and x<='Z':
        chars=chars+1
    elif x>='0' and x<='9':
        digits=digits+1
    elif x==" ":
        words=words+1
print("No of Words=",words+1)
print("No of chars=",chars)
print("No of digits=",digits)