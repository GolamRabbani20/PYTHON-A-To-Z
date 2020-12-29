def insertNodeAtHead(head, data):
    NewNode = SinglyLinkedListNode(data)
    if head != None:
        NewNode.next = head
        head = NewNode
    return NewNode