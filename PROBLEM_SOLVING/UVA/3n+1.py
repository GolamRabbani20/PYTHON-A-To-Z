n=int(input("Enter a number:"))
c=0
max=0
for i in range(1,n+1):
    k=i
    p=c
    while(k!=1):
         if k%2==0:
             k=k/2
         else:
             k=3*k+1
         c+=1

    if max<p:
        max=p
