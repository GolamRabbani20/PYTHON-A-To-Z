def has_cycle(head):
    temp = current = head
    while current != None and current.next != None:
        temp = temp.next
        current = current.next.next
        if current == temp:
           return 1
    return 0