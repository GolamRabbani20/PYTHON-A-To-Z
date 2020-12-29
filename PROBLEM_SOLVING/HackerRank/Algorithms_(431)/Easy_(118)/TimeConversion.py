x=input()
h,m,s=map(int,x[:-2].split(':'))
k=x[-2:].upper() #am/pm
h=h%12+(k=='PM')*12
print(('%02d:%02d:%02d')%(h,m,s))
