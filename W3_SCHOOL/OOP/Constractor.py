class bangla:
    Name=""
    Age=""
    Roll=""
    Section=""

    def __init__(self,Name,Age,Roll,Section):
        self.Name=Name
        self.Roll=Roll
        self.Age=Age
        self.Section=Section

    def dis(self):
        print(f"Name:{self.Name}\nAge:{self.Age}\nRoll:{self.Roll}\nSection:{self.Section}\n")
for i in range(3):
    Name=input("Enter your Name:")
    Age=int(input("Enter your AgeL:"))
    Roll=int(input("Enter your roll:"))
    section=input("Enter your section:")
    s=bangla(Name,Age,Roll,section)
    print("\n")
    s.dis()


