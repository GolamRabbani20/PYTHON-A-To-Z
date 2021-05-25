def reverse(head):
   while head.next!=None:
      #Swap pointer
      head.next, head.prev, head = head.prev,head.next, head.next
   head.next, head.prev = head.prev, None
   return head