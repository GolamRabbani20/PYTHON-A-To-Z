def UsingPlusMinusOperation(a,b):
    print("Using Plus Minus Operation")
    print("Before swapping:", a, b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping:",a,b,'\n')


def UsingMultiplicationDivisionOperation(a,b):
    print("Using Multiplication Division Operation")
    print("Before swapping:", a, b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping:",a,b,'\n')


def UsingXOR(a,b):
    print("Using XOR Operation")
    print("Before swapping:", a, b)
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("After swapping:", a, b, '\n')

    
a, b = map(int,input().split())
UsingPlusMinusOperation(a,b)
UsingMultiplicationDivisionOperation(a,b)
UsingXOR(a,b)
