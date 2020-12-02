#Implement a Libary management system which will handle the flowing tasks:
#.Customer should be able to dispaly the all books available in tha libary
#.Handel the process when a customer request to borrow a book
#.Update the libary collection when the customer returns a book

#Solve:
#Libary class=> display all books,Update book list,to lend book
#Customer class=>request for book,return book

class Libary:
    def __init__(self,Booklist):
        self.BookList=Booklist


    def displayAllBooks(self):
        print("The Available Books:")
        for k in self.BookList:
            print(k)

    def AddBook(self,returnedBook):
        print("Thanks for returning the Book.")
        self.BookList.append(returnedBook)



    def LendBook(self,requestedBook):
        if requestedBook in self.BookList:
            print("Your request has been accepted.You have Borrowed the Book.")
            self.BookList.remove(requestedBook)
        else:
            print("Sorry!The Book out of Available Book list,Please try again.")

class Customer:
    def requestForBook(self):
        requestedBook=input("Enter the request Book:")
        return requestedBook
    def returnBook(self):
        returnedBook=input("Enter the returned Book:")
        return returnedBook


libary=Libary(["Introduction to C","Introduction to C++","Introduction to Java","Problem Solving"])
customer=Customer()
while True:
    print("1.Display All Book.")
    print("2.Request for Borrow book.")
    print("3.Return Book.")
    print("4.Exit")
    n=int(input("Chose Your option:"))
    print()
    if n is 1:
        libary.displayAllBooks()
    elif n is 2:
        requestedBook=customer.requestForBook()
        libary.LendBook(requestedBook)
    elif n is 3:
        returnedBook=customer.returnBook()
        libary.AddBook(returnedBook)
    elif n is 4:
        exit(0)
    print()

