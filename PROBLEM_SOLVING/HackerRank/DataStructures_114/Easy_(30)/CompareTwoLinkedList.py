def compare_lists(llist1, llist2):
    temp1 = llist1
    temp2 = llist2
    while temp1 and temp2:
        if temp1.data == temp2.data:
            temp1 = temp1.next
            temp2 = temp2.next
        else:
            return 0
    if temp1 == temp2:
        return 1
    else:
        return 0