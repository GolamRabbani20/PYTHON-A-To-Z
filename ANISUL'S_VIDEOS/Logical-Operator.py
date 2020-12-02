x=200
y=500
z=-70

if x>y and x>z:
    print(x)

elif y>x and y>z:
    print(y)
else:
    print(z)

p=input("Enter a character:")

if p=='a' or p=='e' or p=='i' or p=='o' or p=='u' or p=='A' or p=='E' or p=='I' or p=='O' or p=='U':
    print("P is vowel")

else:
    print("P is consonant")