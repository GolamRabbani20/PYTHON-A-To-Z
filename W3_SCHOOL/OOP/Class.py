class myclass:
    Roll=""
    Name=""
    Age=""

s=myclass()
#print(isinstance(s,myclass))

s.Name="Rabbani"
s.Age=20
s.Roll=120

print(f"Roll:{s.Roll}\nName={s.Name}\nAge:{s.Age}")

str1=str(input("Enter a string:"))
while len(str1)>1:
   result=1
   for char in str1:
    result*=int(char)
    str1=str(result)
print(str1)