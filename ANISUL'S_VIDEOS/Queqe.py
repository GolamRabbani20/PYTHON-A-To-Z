from collections import deque
Bank=deque(["x","y","Z","Kalom","Python","Java"])
print(Bank)
Bank.popleft()
Bank.popleft()
print(Bank)

for i in range(int(input("Enter no of push:"))):
    Bank=deque([input("Enter elements:")])
print(Bank)