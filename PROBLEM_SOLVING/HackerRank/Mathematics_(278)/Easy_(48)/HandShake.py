def HandShake(n):
    handshake = 0
    for k in range(1,n):
        handshake += n-k
    return handshake

for i in range(int(input())):
    print(HandShake(int(input())))