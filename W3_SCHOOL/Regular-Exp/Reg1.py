import re
tex= "I love Lazina"
x=re.search("^I.*Lazina$",tex)
if x:
    print("Yes! We have matched")
else:
    print("No Matched")