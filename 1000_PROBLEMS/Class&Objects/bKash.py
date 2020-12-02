class bKash:
    def __init__(self,a):
        self.value=a
        self.lst=[]
        self.Balance=0

    def sendMoney(self):
        if self.Balance<self.value:
            print("Insufficient Balance!")
            exit(0)
        else:
            return self.Balance-self.value

    def Cash_In(self):
        self.lst.append(a)
        return self.Balance+sum(self.lst)

    def Cash_Out(self):
        if self.Balance<(self.value+self.value/50):
            print("Insufficient Balance!")
            exit(0)
        else:
          print("Sending Successful.")
          return self.Balance-(self.value+self.value/50)

m=1
k=1
while m!=0:
    print("bKash")
    print("1.Send Money")
    print("2.Cash In")
    print("3.Cash Out")
    print("4.My bKash")
    print("5.Payment")
    print("0.Logout")
    print()

    n=int(input("Chose your option:"))
    if n==1:
        s=input("Enter receiver bKash number:")
        a=int(input("Enter amount:"))
        k = bKash(a)
        pin=int(input("Enter pin:"))
        print("available balance:",k.sendMoney())


    elif n==2:
        a = int(input("Enter amount:"))
        k = bKash(a)
        print("Cash In Successful.")
        print("New Balance:", k.Cash_In())

    elif n==3:
        s = input("Enter Personal/Agent number:")
        a = int(input("Enter amount:"))
        k = bKash(a)
        pin = int(input("Enter pin:"))
        print("available balance:", k.Cash_Out())
        print("Cash Out Successful.")

    elif n==4:
        print("1.Profile")
        print("2.Mini Statement")
        print("0.Main Manu")
        k=int(input("Chose option:"))
        while k!=0:
            if k==1:
                print("Name:Md Golam Rabbani\nAge:20 Years\nOccupation:Student")
            elif n==2:
                pass
            elif n==0:
                print("bKash")
                print("1.Send Money")
                print("2.Cash In")
                print("3.Cash Out")
                print("4.My bKash")
                print("5.Payment")
                print("0.Logout")
                print()

                n = int(input("Chose your option:"))
            else:
                print("Invalid Chose!")


    elif n==0:
        exit(0)

    else:
        print("Invalid Chose!")