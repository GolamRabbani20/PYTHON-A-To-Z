from twilio.rest import Client
Account_sid="AC262ef13f48613ac98bdd4db5d2706f45"
Token="dd461c138b0b3b91822a2a04f5c0aa7a"
PhoneNo="+8801761793058"

for k in range(10):
    client=Client(Account_sid,Token)
    sms=client.messages.create(from_="+16105494187",body="I Love Python.",to=PhoneNo)

#print(sms.sid)
print("Sent Successfully.....")