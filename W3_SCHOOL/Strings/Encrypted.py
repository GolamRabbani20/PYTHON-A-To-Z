from string import ascii_lowercase as p
msg=input("Enter a massage:")
msg=msg.lower()
Encrypted_msg=""
for k in msg:
    if k in p:
        k2=122-ord(k)
        Encrypted_msg+=chr(k2+97)
    else:
        Encrypted_msg+=1
print(Encrypted_msg)
