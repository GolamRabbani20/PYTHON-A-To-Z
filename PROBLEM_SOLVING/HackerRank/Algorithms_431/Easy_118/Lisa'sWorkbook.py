def LisasWorkbook(k,chapters):
    k = int(k)
    page = 1
    sp = 0
    for x in chapters:
        for problem in range(1,x+1):
            if page == problem:
                sp += 1
            if (problem % k == 0) or (problem == x):
                page += 1
    return sp

n,k = input().split()
chapters=list(map(int,input().strip().split()))
print(LisasWorkbook(k,chapters))

"""N, K = map(int, input().split())
T = map(int, input().split())

count = 0 
chapter = 0  
page = 1   
problem = 1 

while chapter < N:
    if problem <= page and page <= min(problem + K - 1, T[chapter]):
        count += 1
    page += 1
    problem += K
    if problem > T[chapter]: # next chapter
        page += 1
        problem = 1
print (count)"""