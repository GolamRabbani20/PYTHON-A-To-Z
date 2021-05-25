def deleteNode(head, position):
    if position == 0:
        head = head.next
    else:
        temp = head
        prev = None
        k = 0
        while k < position:
            prev = temp
            temp = temp.next
            k += 1
        prev.next = temp.next
        temp.next = None
        del temp
    return head

##############################################
def deleteNode2(head, position):
    if position == 0:
        head = head.next
    else:
        temp = head
        k = 0
        while k < position - 1:
            temp = temp.next
            k += 1
        temp.next = temp.next.next

    return head