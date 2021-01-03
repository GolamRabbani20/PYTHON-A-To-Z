# Find ont the n tomo fibonacci number
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    Sum = fibo(n - 1) + fibo(n - 2)
    return Sum
print(fibo(int(input())))
