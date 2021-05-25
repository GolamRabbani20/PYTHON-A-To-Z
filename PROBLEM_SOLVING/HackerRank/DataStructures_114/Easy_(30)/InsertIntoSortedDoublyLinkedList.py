def sortedInsert(head, data):
    Node = DoublyLinkedListNode(data)
    if head == None:
        head = Node
    elif data < head.data:  # Insert at beginning position
        Node.next = head
        head.prev = Node
        head = Node
    else:
        temp = head
        while temp.next != None and temp.data < data:      # Traverse to specific position
            temp = temp.next

        if temp.next == None and temp.data < data:         # Insert end of the list
            temp.next = Node
            Node.prev = temp

        else:                                              # Insert specific position
            prevNode = temp.prev
            prevNode.next = Node
            Node.prev = prevNode
            Node.next = temp
            temp.prev = Node
    return head