class person:
      def __init__(self,fname,lname):
          self.firstnmae=fname
          self.lastname=lname

      def dis(self):
          print(self.firstnmae,self.lastname)


class student(person):
    def __init__(self, fname, lname):
      super().__init__(fname, lname)
    print("lalallal")


k=student("Md Golam","Rabbani")
k.dis()