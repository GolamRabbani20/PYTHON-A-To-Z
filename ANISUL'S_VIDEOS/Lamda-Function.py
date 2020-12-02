'''
def cal(a,b):
    r=a*a + 2*a*b + b*b
    return r

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

print("Result is = ",cal(a,b))
'''

#(lambda parameter: Expression)(value)

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
result=(lambda a,b : a*a + 2*a*b + b*b ) (a,b)
print("Result is = ",result)

print("Value of lambda:",(lambda x:x*x*x*x*x*x)(39))