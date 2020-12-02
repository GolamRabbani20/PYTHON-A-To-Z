class Libary:
    def __init__(self,BookList):
        self.BookList=BookList

    def AddBook(self,returnedBook):
        print("Thank you for returning book.")
        self.BookList.append(returnedBook)

    def RendBook(self,requestedBook):
        if requestedBook in self.BookList:
            print("Your request has been accepted.")
            self.BookList.remove(requestedBook)
        else:
            print("Sorry! The Book is not available in list,Please try again.")


    def DisplayBooks(self):
        i=1
        print("The Available Books:")
        for Book in self.BookList:
            print(i,end=" ")
            print(Book)
            i=i+1

class Custome:
    def RequestedBook(self):
        requentedBook=input("Enter a Book Name:")
        return requentedBook

    def ReturnBook(self):
        returnedBook=input("Enter returned Book name:")
        return returnedBook

libary=Libary(["C++","Java","OOP","C","Python"])
customer=Custome()
while True:
    print("1.Display all Books.")
    print("2.Borrow book.")
    print("3.Returned Book.")
    print("4.Exit.")
    UserChose=int(input("Chose Your Option:"))
    print()

    if UserChose == 1:
        libary.DisplayBooks()

    elif UserChose == 2:
        requestedBook=customer.RequestedBook()
        libary.RendBook(requestedBook)

    elif UserChose == 3:
        BorrowBook=customer.ReturnBook()
        libary.AddBook(BorrowBook)

    elif UserChose == 4:
        exit(0)

    else:
        print("Invalid Chose! Please try again.")

    print()





