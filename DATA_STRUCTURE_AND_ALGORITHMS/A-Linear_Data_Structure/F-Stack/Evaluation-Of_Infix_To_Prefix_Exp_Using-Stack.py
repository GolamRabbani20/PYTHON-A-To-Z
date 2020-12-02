class Stack:
    def __init__(self):
        self.OpStack=[]
        self.Top=-1

    def PushOperend(self,operand):
        self.Top+=1
        self.OpStack.append(operand)

    def PopOperand(self):
        if self.Top==0:
            return self.OpStack.pop()
        else:
            return self.OpStack.pop()

ob=Stack()
exp=input("Enter expression:").split()
for k in reversed(exp):
    if k>='0' and k<='9':
        ob.PushOperend(int(k))
    else:
        if k=='+':
            op1=ob.PopOperand()
            op2=ob.PopOperand()
            result=op1+op2
            ob.PushOperend(result)

        elif k=='-':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op1 - op2
            ob.PushOperend(result)

        elif k=='*':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op1 * op2
            ob.PushOperend(result)

        elif k=='/':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op1 / op2
            ob.PushOperend(result)

        elif k=='^':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op1 ** op2
            ob.PushOperend(result)

res=ob.PopOperand()
print(res)














