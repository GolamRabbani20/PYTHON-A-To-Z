def Quicksort(a):
    less = []
    equal = []
    gratter = []
    if len(a)>1:
        Pivot=a[0]
        for k in a:
            if k<Pivot:
                less.append(k)
            elif k==Pivot:
                equal.append(k)
            else:
                gratter.append(k)

        return Quicksort(less)+Quicksort(equal)+Quicksort(gratter)
    else:
        return a

a=[7,6,10,5,9,2,1,15,7]
print(Quicksort(a))