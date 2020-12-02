"""
Define a function that accept a string number as an argument and returns a signal
number as an output after reversely multiplying the elements of the number
Example:An input 512 will return an output 0,Because
5x1x2=10
1x0=0

Similarly input 642 will return 6
6x4x2=48
4x8=32
3x2=6
"""

str1=str(input("Enter a string:"))
while len(str1)>1:
   result=1
   for char in str1:
    result*=int(char)
    str1=str(result)
print(str1)