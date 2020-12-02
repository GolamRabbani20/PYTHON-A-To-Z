class Postfix:
    def __init__(self):
        self.Stack=[]
        self.Top=-1

    def PushOperend(self,item):
        self.Top+=1
        self.Stack.append(item)

    def PopOperand(self):
        if self.Top==0:
            result=self.Stack.pop()
            self.Top -= 1
        else:
          result=self.Stack.pop()
          self.Top -= 1
        return result


ob=Postfix()
data=input("Enter Postfix expression::").split()
for k in data:
    if k.isdigit():
        ob.PushOperend(int(k))

    else:
        if k == '+':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2 + op1
            ob.PushOperend(result)

        elif k == '-':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2 - op1
            ob.PushOperend(result)

        elif k == '*':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2 * op1
            ob.PushOperend(result)

        elif k == '/':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2 / op1
            ob.PushOperend(result)

        elif k == '^':
            op1 = ob.PopOperand()
            op2 = ob.PopOperand()
            result = op2 ** op1
            ob.PushOperend(result)

res = ob.PopOperand()
print(res)