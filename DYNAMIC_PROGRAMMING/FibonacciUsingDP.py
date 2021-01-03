# Find ont the n tomo fibonacci number

#................................................................Method-01 (Using formula, Fn = {[(√5 + 1)/2] ^ n} / √5)
import math
def fibonacciMethod1(n):
    p = (1 + math.sqrt(5)) / 2
    print(p)
    return round((p**n) / math.sqrt(5))

#.....................................................................Method-02 (Dynamic programming Bottom-Up approach)
def fibonacciMethod2(n):
    x = [0, 1]
    for i in range(2, n+1):
        x.append(x[i-1] + x[i-2])
    return x[n]

#..................................................................................Method 3 ( Space Optimized Method-02)
def fibonacciMethod3(n):
    first = 0
    second = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2,n+1):
        result = first + second
        first = second
        second = result
    return second

n = int(input())
print("Method-01 = ",fibonacciMethod1(n))
print("Method-02 = ",fibonacciMethod2(n))
print("Method-03 = ",fibonacciMethod3(n))