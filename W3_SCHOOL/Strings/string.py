a="""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""

print(len(a))
print(a.upper())

x=" Hello Bangladesh "
y="Dhaka is a big city-1998"

print(x.lower())
print(x.upper())
print(x)
print(x.strip())
print(x.replace("Hello","I love"))
print(x.split("."))
print("popular" in a)
print("Number of char/word=",y.count("a"))

print(a.count("p",0,100))
print(y.center(5))

z=x+y
print(z)

p=x+" "+y
print(p)

b = "Hello, World!"
print(b[-5:-2])

j=5j
q=10j*2j
h=j*q
print(h)

quantity=10
item_no=201
price=2564

myorder="Quantity={}\nItem No={} \nPrices={}"
my_order="Dolars={2}\t Item-no={1}\t Quantity={0}"

print(myorder.format(quantity,item_no,price))
print(my_order.format(quantity,item_no,price))

print("\'I love Python\'")
print("I am a\bBsc")

tex="Banana"
print(tex.center(100))
print(tex.center(20, "O"))