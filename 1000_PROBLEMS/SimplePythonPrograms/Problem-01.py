#The program takes the elements of the list one by one and displays the average of the elements of the list

n = int(input("Enter the number of elements:"))
x = []
for i in range(n):
    s = int(input("Enter element of the list:"))
    x.append(s)

avg = sum(x) / n

print("The average value is:",round(avg,2))
print("The average of the list:","%.5f" %avg)