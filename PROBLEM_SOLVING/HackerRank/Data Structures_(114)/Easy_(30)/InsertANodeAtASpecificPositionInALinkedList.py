def insertNodeAtPosition(head, data, position):
    NewNode = SinglyLinkedListNode(data)
    temp = head
    k = 0
    while k < position:
        prev = temp
        temp = temp.next
        k += 1
    prev.next = NewNode
    NewNode.next = temp
    return head