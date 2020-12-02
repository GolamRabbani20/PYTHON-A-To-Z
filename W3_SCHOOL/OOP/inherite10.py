class A:
    def dis1(self):
        print("I love you A.")

class B:
    def dis1(self):
        print("I am in B")

class C(A,B):
    pass


k=C()

k.dis1()