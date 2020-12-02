class st:
    Name=""
    ID=""
    Age=""

    def setvalue(self,Name,Age,ID):
        self.Name=Name
        self.Age=Age
        self.ID=ID

    def display(self):
         print(f"Name:{self.Name}\nAge:{self.Age}\nID:{self.ID}\n")

s=st()
s.setvalue("Habib",15,10147)
s.display()

s1=st()
s1.setvalue("Rabbani",21,1234)
s1.display()