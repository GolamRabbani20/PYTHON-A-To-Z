#Parent class,Super class,Base class
class nokia:
      def massage(self):
          print("I love you jan")
      def call(self):
           print("Call me any time")
      def talktime(self):
          print("You have no talktime anymore")

#Child class,Sub class,Derived class
class samsang(nokia):
    #massage,call,talktime mathod gula akhane chole asce
    def tax(self):
        print("Paid your tax")
    def callrate(self):
        print("Your call rate is 45 poysha")

n=nokia()
n.call()
n.massage()
n.talktime()

print("\nSammsang Class\n")
s=samsang()
s.callrate()
s.tax()
s.callrate()
s.massage()
s.call()
s.talktime()

print(issubclass(samsang,nokia))
