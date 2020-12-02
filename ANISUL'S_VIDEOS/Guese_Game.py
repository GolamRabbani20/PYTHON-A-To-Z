from random import randint

for i in range(1,101):
    GuessNumber=int(input("\nEnter a number from 1 to 10:"))
    RandomNumber=randint(1,10)

    if RandomNumber==GuessNumber:
       print("\nCongratulation! You have won the game.")
       print("The RandomNumber is ", RandomNumber)

    else:
      print("\nSorry! You have lost the game.")
      print("The RandomNumber is ",RandomNumber)
