def reverse(head):
    if head is None:
        return
    prevNode = None
    CurrentNode = head
    NextNode = head
    while NextNode is not None:
        NextNode = CurrentNode.next
        CurrentNode.next = prevNode
        prevNode = CurrentNode
        CurrentNode = NextNode
    head = prevNode
    return head