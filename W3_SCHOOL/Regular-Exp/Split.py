import re
txt="Programming is my passion"
k=re.split("\s",txt)
print(k)
x=re.split("\s",txt,2)
print(x)

p="webIwebwebwebamwebwebRabbaniwebweb"
t=re.split("web",p)
print(t)
