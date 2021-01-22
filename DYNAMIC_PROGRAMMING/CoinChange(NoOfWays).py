def FindNoOfWays(C, A):
    llen = len(C)
    table = [0 for k in range(A+1)]
    table[0] = 1
    for i in range(llen):
        for j in range(C[i],A+1):
            table[j] = table[j] + table[j-C[i]]
    return table[A]

C = list(map(int,input().split()))
A = int(input())
print(FindNoOfWays(C, A))



"""def FindNoOfWays(coins,w):
    llen = len(coins)
    table = [[0 for x in range(llen)] for x in range(w+1)]

    for i in range(llen):
        table[i][0] = 1

    for i in range(llen):
        for j in range(n + 1):
            if coins[i]>j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] + table[i][j-coins[i]]
    return table[n][llen - 1]

coins =  [2,3,5,10]        
n = int(input())
print(FindNoOfWays(coins,n))"""