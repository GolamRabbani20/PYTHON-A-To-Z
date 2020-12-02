def DrawingBook(n,p):
    return min(p//2,n//2-p//2)

n=int(input())
p=int(input())
print(DrawingBook(n,p))

