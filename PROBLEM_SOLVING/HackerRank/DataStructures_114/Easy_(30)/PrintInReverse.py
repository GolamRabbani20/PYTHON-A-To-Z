def reversePrint(head):
    if head is None:
        return
    reversePrint(head.next)
    print(head.data)

#Solution 2
def reversePrint2(head):
    temp = head
    lst = []
    while temp != None:
        lst.append(temp.data)
        temp = temp.next
    for k in lst[::-1]:
        print(k)