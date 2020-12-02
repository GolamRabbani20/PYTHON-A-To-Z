#Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints it
class light:
    def __init__(self):
        self.String=""
    def getInput(self):
        self.String=input("Enter a string:")
    def OutPut(self):
        print("The string is:",self.String)

k=light()
k.getInput()
k.OutPut()

'''
class roja:
    def __init__(self,s):
        self.s=s
    def dis(self):
        print("The string is:",self.s)


n=input("Enter a string:")
k=roja(n)
k.dis()
'''