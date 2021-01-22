def getNode(head, positionFromTail):
    temp = head
    len = 0
    while temp:
        len += 1
        temp = temp.next
    k = 0
    while k <= len -  positionFromTail - 1:
        if k == len -  positionFromTail - 1:
            return head.data
        k += 1
        head = head.next