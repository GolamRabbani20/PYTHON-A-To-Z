x=dict([
    ("first",1),
    ("second",2),
    ("Third",3),
    ("Fourth",4)
])

print(x)

y=dict(one=1,two=2,three=3,four=4)

k=dict(y.items())
m=y.copy()
print(k)

p={
    45:"kalksh",
    "lata":"tree",
    "marks":"pass"
}
print(p.get(2))

q={}
n=dict()
print(n)
print(q)

u={5:{"name":"Raton","age":25},
   2:{"name":"latip","age":20}}

print(u[5]["age"])


s={
    "class":{
        "student": {
            "name":"lata",

            "marks":{
                "physics":25,
                "history":120
            }
        }

        }
    }

print(s["class"]["student"]["marks"]["history"])

s1={"k1":1,"k2":2,"k3":40}
s2={"k2":2,"k1":1,"k3":40}

print(s1==s2)

print(s1.clear())



t={"name":"Rabbani","salary":20000}

print("Ans:",del t["salary"])
print(t)