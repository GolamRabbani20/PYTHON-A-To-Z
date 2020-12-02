student={
    1 : "kalam",
    2 : "majj",
    3 : "lata",
    4 :"tamim",
    "model":23659
}
student[5]="lazia"
print(len(student))

student.pop(2)

if 2 in student:
    print("Yes")
else:
    print("No")

print(student["model"])

print(student.get(3))
student[7]="rabbani"

print("\n")
for i in student.values():
   print(i)

print("\n")
for i ,j in student.items():
   print(i,j)

color={
    0:"red",
    1:"Green",
    2:"yellow",
    3:"blue",
    4:"white",
    5:"pink",
    6:"blue"
}

color.popitem()
print(color)



sts={
    1:"alu",
    2:"potol",
    3:"kli"
}

my=sts.copy()
m=dict(sts)

sts.clear()
print(sts)

print(my)
print(m)

family={
    "child1":{
        "name":"Habib",
        "Age":52,
         "Class":"Two"
    },
    "child2": {
        "name": "Hemel",
        "Age": 22,
        "Class": "Three"
    },

"child3":{
        "name":"forid",
        "Age":12,
         "Class":"five"
    }
}
print("Family1=",family)

child1={
    "hight":5.5,
      "weight":"50kg",
       "Age":25
}

child2={
    "hight":6.5,
      "weight":"60kg",
       "Age":15
}

child3={
    "hight":7.5,
      "weight":"55kg",
       "Age":20
}

Family={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print("Family2=",Family)

corona=dict(Brand="lau",model="kal205",year=2050)
print(corona)
print(corona.keys())
