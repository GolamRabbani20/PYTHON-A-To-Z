n=int(input())
for row in range(1,n+1):
    for col in range(1,n-row):
        print(end=" ")

    for col in range(1,row+1):
        print(col,end="")

    print()