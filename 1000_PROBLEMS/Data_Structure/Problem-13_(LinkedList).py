#Python Program to Print the Alternate Nodes in a Linked List without using Recursion
class Noda:
    def __init__(self,datu):
        self.Datu=datu
        self.nexto=None

class LingoListo:
    def __init__(self):
        self.heada=None

    def AddNoda(self,NewNoda):
        if self.heada is None:
            self.heada=NewNoda
        else:
            lastNoda=self.heada
            while lastNoda.nexto!=None:
                lastNoda=lastNoda.nexto
            lastNoda.nexto=NewNoda

    def Alternato(self):
        StartiNoda=self.heada
        while StartiNoda:
            print(StartiNoda.Datu, end=" ")
            if StartiNoda.nexto is not None:
               StartiNoda=StartiNoda.nexto.nexto
            else:
                break

    def displa(self):
        CurrentoNodo=self.heada
        while CurrentoNodo is not None:
            print(CurrentoNodo.Datu,end=" ")
            CurrentoNodo=CurrentoNodo.nexto
        print()


lst=LingoListo()
n = int(input("Enter number of nodes:"))
for i in range(n):
    datu = input("Enter value of nodes:")
    noda = Noda(datu)
    lst.AddNoda(noda)

print("\nThe Linked List:", end=" ")
lst.displa()
print("The Alternate Item in the list:", end=" ")
lst.Alternato()