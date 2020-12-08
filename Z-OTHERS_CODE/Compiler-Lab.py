def Compiler_Lab17(x,n):
    count=0
    if n==1 and x=='a':
        print("Acceptable")
    else:
        for i in x[1:]:
            if i=='b':
                count+=1
        if count==n-1:
            print("Acceptable")

        else:
            print("Not acceptable")

x=input()
Compiler_Lab17(x,len(x))