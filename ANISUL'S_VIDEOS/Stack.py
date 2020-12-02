Degree=[]  #Degree is a list which works as stack by push=append & pop operation

Degree.append("Learn C")
Degree.append("Learn C++")
Degree.append("Learn Java")
Degree.append("Learn Python")
Degree.append("Learn English")
print("Before pop1=",Degree)

Degree.pop()
print("After pop1=",Degree)
print("Now the top element is:",Degree[-1])


for i in range(int(input("Enter no of push:"))):
    Degree.append(input("Enter a string: "))
print("Before pop2=",Degree)
print("Number of elements of the stack now:",len(Degree))


for i in range(int(input("Enter number of pop:"))):
    Degree.pop()

if not Degree:
    print("Stack Underflow")

else:
    print("After pop2=", Degree)
