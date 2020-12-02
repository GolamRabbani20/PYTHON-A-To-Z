#Khairul basic math page(82 problem-07)
n1,n2=input("Enter size of Iron & Ispat:").split()
n1=int(n1)
n2=int(n2)
k1=n1
k2=n2
if n1<n2:
    while n1!=0:
        rem=n2%n1
        n2=n1
        n1=rem
    print("Largest Pieces is:",n2)
    print("The Pieces of Iron:",k1/n2)
    print("The Pieces of Ispat:", k2/n2)

else:
    while n2!=0:
        rem=n1%n2
        n1=n2
        n2=rem
    print("Largest Pieces is:", n1)
    print("The Pieces of Iron:",k1/n1)
    print("The Pieces of Ispat:",k2/n1)
