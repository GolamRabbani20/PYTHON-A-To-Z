class students:
      roll=""
      gpa=""
      name=""

korim=students()
x=students()
k=students()

#print(isinstance(korim,students)) #check object
korim.gpa=3.5
korim.roll=102

x.name="Rakib"
x.roll=3267278
x.gpa=3.56

k.name=input("Enter your name:")
k.gpa=3.145
k.roll=3267278


print(f"Roll={korim.roll}\nGPA={korim.gpa}")
print("\n")
print(f"Roll={x.roll}\nGPA={x.gpa}\nName={x.name}")
print("\n")
print(f"Roll={k.roll}\nGPA={k.gpa}\nName={k.name}")
