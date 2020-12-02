import re
txt="Bangladesh is our mother Land"
x=re.findall("[a-g]",txt)
print(x)

a=re.findall("our",txt)
print(a)