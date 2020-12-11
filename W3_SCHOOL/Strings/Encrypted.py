from string import ascii_lowercase
msg=input("Enter a massage:")
msg=msg.lower()
Encrypted_msg=""
for k in msg:
    if k in ascii_lowercase:
        k2=122-ord(k)
        Encrypted_msg+=chr(k2+97)
    else:
        Encrypted_msg+=1
print(Encrypted_msg)
