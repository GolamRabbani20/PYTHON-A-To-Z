try:
   n=int(input("Enter a number:"))
   x=100/n
   print(x)
except ZeroDivisionError:
    print("Invalid Input")
except TypeError:
    print("Invalid Input1")

finally:
    print("I am student")
    if n<=50:
      print("not")