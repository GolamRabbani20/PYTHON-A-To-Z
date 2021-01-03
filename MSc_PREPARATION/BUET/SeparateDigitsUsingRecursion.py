def SeparateDigits(n):
    digit = n % 10
    n = n / 10
    if n != 0:
         SeparateDigits(n)
    print(digit,end=" ")

n = int(input())
SeparateDigits(n)