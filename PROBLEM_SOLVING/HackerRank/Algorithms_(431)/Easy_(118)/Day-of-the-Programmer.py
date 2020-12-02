y=int(input())
if y>=1700 and y<=1917:
    if y%4==0:
        n=256-244
        print(str(n)+".09."+str(y))

    else:
        n = 256-243
        print(str(n)+".09."+str(y))

elif y==1918:
    n=26
    print(str(n) + ".09." + str(y))

else:
    if (y%400==0 ) or (y%100!=0 and y%4==0):
        n = 256 - 244
        print(str(n) + ".09." + str(y))

    else:
        n = 256 - 243
        print(str(n) + ".09." + str(y))