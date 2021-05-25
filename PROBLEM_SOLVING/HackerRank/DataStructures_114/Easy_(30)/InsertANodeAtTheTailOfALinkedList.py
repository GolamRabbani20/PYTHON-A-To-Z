def insertNodeAtTail(head, data):
    NewNode = SinglyLinkedListNode(data)
    if head is None:
        head = NewNode
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = NewNode
    return head
