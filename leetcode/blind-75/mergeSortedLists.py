from LinkedList import LinkedListMethods
def mergeSortedLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    ptr1 = head1
    ptr2 = head2
    finalHead = None
    finalTail = None
    while ptr1!=None and ptr2!=None:
        if ptr1.val<=ptr2.val:
            if finalHead == None and finalTail == None:
                finalHead = ptr1
                finalTail = ptr1
            else:
                finalTail.next = ptr1
                finalTail = ptr1
            ptr1 = ptr1.next
        else:
            if finalHead == None and finalTail == None:
                finalHead = ptr2
                finalTail = ptr2
            else:
                finalTail.next = ptr2
                finalTail = ptr2
            ptr2 = ptr2.next
    if ptr1!=None:
        finalTail.next = ptr1
    if ptr2!=None:
        finalTail.next = ptr2
    return finalHead

ll = LinkedListMethods()
head1 = ll.inputLL()
head2 = ll.inputLL()
mergedHead = mergeSortedLists(head1,head2)
ll.printLL(mergedHead)


            