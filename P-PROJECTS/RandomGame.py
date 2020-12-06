from numpy import random as rd
def RandomGame(n):
  Score=0
  A=rd.randint(1,100, size=(15))
  print("Random Array is:",A)
  print("Your matching numbers:",end="")
  for k in A:
      if n.count(k):
          print(k,end=" ")
          Score+=k
  return Score
#=======================================================================================================================
x=[]
print("Please,Enter any ten numbers(1-100)")
print("-----------------------------------")
for i in range(1,11):      #n=list(map(int,input("Enter any ten numbers(1-100):").split()))
    if i==1:
        s=int(input("Enter "+str(i)+"st number:"))
        x.append(s)
    elif i==2:
        s=int(input("Enter "+str(i) + "nd number:"))
        x.append(s)
    elif i==3:
        s=int(input("Enter "+str(i)+"rd number:"))
        x.append(s)
    else:
        s=int(input("Enter "+str(i)+"th number:"))
        x.append(s)

m=RandomGame(x)
if m>=100:
  print("\nCongratulations! You have won the game,Your score is ",m)
else:
  print("\nSorry! You have lose the game because your score is less than 100.Your score is",m)

while True:
    x=[]
    ch=input("Do you want to play again(y/n):")
    print()
    if ch.upper()=="Y":
        print("Please,Enter any ten numbers(1-100)")
        print("-----------------------------------")
        for i in range(1,11):      #n=list(map(int,input("Enter any ten numbers(1-100):").split()))
            if i==1:
                s=int(input("Enter "+str(i)+"st number:"))
                x.append(s)
            elif i==2:
                s=int(input("Enter "+str(i)+"nd number:"))
                x.append(s)
            elif i==3:
                s=int(input("Enter "+str(i)+"rd number:"))
                x.append(s)
            else:
                s=int(input("Enter "+str(i)+"th number:"))
                x.append(s)

        m=RandomGame(x)
        if m>=100:
          print("\nCongratulations! You have won the game,Your score is ",m)
        else:
            print("\nSorry! You have lost the game because your score is less than 100.Your score is",m)
    else:
        break