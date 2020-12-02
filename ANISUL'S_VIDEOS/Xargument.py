def student(*x):
    print(x[2])
    print(x)
student("Rabbani",1998,3.50,5.6)

def add(*a):
    sum=0
    for n in a:
        sum=sum+n
    print("Summation=",sum)


add(20,36,45,69,5285,22,21)
add(20,36,45,22,21)
add(20,36,45,69,5285,22)