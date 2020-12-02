class exam:
    Name:""
    Roll=""
    Reg=""
    Section=""
    Group=""

    def __init__(self, n, r, reg, s, g):
        self.Name = n
        self.Roll = r
        self.Reg = reg
        self.Section = s
        self.Group = g

    def dis(self):
       print(f"Name:{self.Name}\nRoll:{self.Roll}\nReg:{self.Reg}\nSection:{self.Section}\nGroup:{self.Group}\n")


n=int(input("Enter n:"))
for i in range(n):
    n=input("Enter your name:")
    r=int(input("Enter your roll:"))
    reg=int(input("Enter your registration no:"))
    s=input("Enter your section:")
    g=input("Enter your group:")
    print("\n")
    c=exam(n,r,reg,s,g)
    c.dis()

#s=exam("Alif",101,12345,"B1","Arts")
#s.dis()

#print(f"Name:{s.Name}\nRoll:{s.Roll}\nReg:{s.Reg}\nSection:{s.Section}\nGroup:{s.Group}\n")

#s1=exam("Emon",105,1723,"B5","Science")
#s1.dis()

#print(f"Name:{s1.Name}\nRoll:{s1.Roll}\nReg:{s1.Reg}\nSection:{s1.Section}\nGroup:{s1.Group}\n")