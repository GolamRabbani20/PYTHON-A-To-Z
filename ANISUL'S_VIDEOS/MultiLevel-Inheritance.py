#Class_A <--- Class_B <--- Class_C

class A:
    def display1(self):
        print("Class A")

class B(A):
    def display2(self):
        print("Class B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("Class C")


r=C()
r.display3()
#r.display2()
#r.display1()