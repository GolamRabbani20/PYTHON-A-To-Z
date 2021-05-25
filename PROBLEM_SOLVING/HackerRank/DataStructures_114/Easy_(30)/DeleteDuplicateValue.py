def removeDuplicates(head):
    current = head
    temp = head.next
    while temp != None:
        if current.data == temp.data:
           temp = temp.next
           current.next = temp
        else:
            temp = temp.next
            current = current.next
    return head