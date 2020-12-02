#Python Program to Check if a Date is Valid and Print the Incremented Date if it is
date=input("Enter a date(dd/mm/yy):")
dd,mm,yy=date.split('/')

dd=int(dd)
mm=int(mm)
yy=int(yy)

if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    day=31

elif (mm==4 or mm==6 or mm==9 or mm==11):
    day=30

elif (yy%4==0 and yy%100!=0 or yy%400==0):
    day=29

else:
    day=28

#...........................................

if(mm<1 or mm>12):
    print("Date is invalid!")

elif (dd<1 and dd>day):
    print("Date is invalid!")

elif (dd==day and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented day is:", dd, mm, yy,sep=".")

elif (dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented day is:",dd,mm,yy ,sep=".")

else:
    dd=dd+1
    print("The incremented day is:", dd, mm, yy,sep=".")

