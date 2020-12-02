class person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def ff(self):
        print("I am a boy "+self.name)

k=person("Jamal",25,6.3)
#print(k.name)
#print(k.age)
#print(k.height)
print(k.ff())