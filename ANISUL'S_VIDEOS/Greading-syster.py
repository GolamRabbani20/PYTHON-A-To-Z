n=int(input("Enter your marks: "))
if n>=80 and n<=100:
    print("A+")
elif n>=40 and n<=45:
    print("C")
elif n>=50 and n<=55:
    print("B-")
elif n>=56 and n<60:
    print("B+")

elif n>=70 and n<80:
    print("A")
elif n>=60 and n<=65:
    print("A-")
else:
    print("F")