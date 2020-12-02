import datetime
import myModule
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%I %p %U %Z %j"))

k=datetime.datetime(2020,5,10)
print(k)

p=datetime.tzinfo()
print(p)




myModule.greeting("Jonathan")