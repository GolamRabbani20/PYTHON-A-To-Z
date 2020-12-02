#Python Program to Take in the Marks of 5 Subjects and Display the Grade
a=[]
for i in range(1,6):
    print("Marks of subject-",i ,":")
    x=int(input())
    a.append(x)

avg=sum(a)/5
print("................................")
print("Average value=",avg)

if avg>=33 and avg<40:
    print("Grade:D")
elif avg<33:
    print("Grade:F")
elif avg>=80:
    print("Grade:A+")
elif avg>=70 and avg<80:
    print("Grade:A")
elif avg>=60 and avg<70:
    print("Grade:A-")
elif avg>=50 and avg<60:
    print("Grade:B")
elif avg>=40 and avg<50:
    print("Grade:C")