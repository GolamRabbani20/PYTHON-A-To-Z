import os
#p=open("xxx.py","x")
if os.path.exists("xxx.py"):
    os.remove("xxx.py")
else:
    print("The file is exist!")

k=open("Delete.py","x")