class Stack:
    def __init__(self):
        self.Operand=[]
        self.Top=-1

    def PushOprend(self,Operand):
        self.Top+=1
        self.Operand.append(Operand)

    def PopOperand(self):
        if self.Top==0:
            return self.Operand.pop()
        else:
            return self.Operand.pop()

ob=Stack()
exp=input("Enter a postfix expression:").split()
for k in exp:
    if k.isalpha() or k.isdigit():
        ob.PushOprend(k)
    else:
        if k=='+':
            op1=ob.PopOperand()
            op2=ob.PopOperand()
            result=op2,k,op1
            ob.PushOprend(result)

        elif k=="-":
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2,k, op1
            ob.PushOprend(result)

        elif k=="*":
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2,k, op1
            ob.PushOprend(result)
        elif k=="/":
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result =op2,k,op1
            ob.PushOprend(result)

print(ob.PopOperand())
