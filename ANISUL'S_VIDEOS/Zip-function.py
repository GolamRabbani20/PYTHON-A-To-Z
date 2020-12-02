#Zip function ar kaj hoilo multiple list k tuple akare akta list a convert kora

roll=[101,102,103,104,154,1010]
name=["Rabbani","Habib","Kamal","Hemel","Monir","Ashik"]
age=[22,25,23,20,10,15]
dept=["CSE","BBA","SWE","English","Eco","EEE"]

result=list(zip(roll,name,dept,age,"ABCDEF")) #ABCDEF is sections
print(result)