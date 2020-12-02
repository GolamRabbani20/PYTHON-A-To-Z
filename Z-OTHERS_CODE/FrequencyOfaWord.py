def Maximum_Frequency_of_a_String(x):
    maxx=0
    for i in x:
        if maxx<x.count(i):
            maxx=x.count(i)
            p=i
    print("Maximum frequency=",maxx,"Word=",p)