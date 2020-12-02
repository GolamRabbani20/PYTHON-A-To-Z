import re
txt="It was a rainy day"
x=re.search("\s",txt)
print("The 1st white-space found at position:",x.start())