#Python Program to Find Element Occurring Odd Number of Times in a List
def Odd_number_of_Item(list1):
    result=0
    for i in list1:
        result=result^i
    return result

x=input("Enter a list:")
n=x.split()
m=[]
[m.append(int(k)) for k in n]
print("The element that occurs odd number of times:",Odd_number_of_Item(m))
