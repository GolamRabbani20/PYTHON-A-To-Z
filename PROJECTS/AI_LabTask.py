CoureList = []


def line():
    print('.....................................................................')


def show_menu():
    line()
    print('MENU BAR')
    print('1.Add couse\n2.Show course list\n3.Remove or Unenroll\n4.Exit\n')
    return int(input("Choose your option:"))


while True:
    choice = show_menu()
    line()
    if choice == 1:
        while True:
            ch = input("Do you want to add course(Y/N)?:")
            if ch.upper() == 'Y':
                CoureList.append(input('Enter your course name:'))
                print('Your couse has been added successfully.\n')
            elif ch.upper() == 'N':
                break
            else:
                print("Invalid! Try again.")

    elif choice == 2:
        if len(CoureList) == 0:
            print("Your Course List is empty. Please add your course")
        else:
            k = 1
            print("Your avilable courses are shown bellow")
            for i in CoureList:
                print(str(k), ')', i)
                k += 1

    elif choice == 3:
        if len(CoureList) == 0:
            print("Sorry! Your list is empty.")

        else:
            while True:
                ch = input("Do you want to remove course(Y/N)?:")
                if ch.upper() == 'Y':
                    cn = input('Please, Enter removal course name:')
                    if CoureList.count(cn):
                        CoureList.remove(cn)
                        print(cn, 'has been removed successfully.\n')
                    else:
                        print("Sorry! The course name dose not matched!")

                elif ch.upper() == 'N':
                    break
                else:
                    print("Invalid! Try again.")

    elif choice == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid Choice! Please try again.')