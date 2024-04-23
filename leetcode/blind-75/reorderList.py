from LinkedList import LinkedListMethods

def reorderLL(head):
    # Step-1: If list contains only 1 node or no node, just return 
    if head == None or head.next == None:
        return
    
    # Step-2: Find the middle of the list
    slow , fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    second = slow.next
    slow.next = None

    # Step-3: Reverse the second half
    prev = None
    while(second):
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # At this point prev is storing the head of our reversed second half of the list
    # Step-4: Alternatively merge first half and the second half of the list
    first, second = head, prev
    while second: # checking of second only and not first, because, second list can be smaller than first list by 1 element, but vice-versa is not possible
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next=temp1
        first, second = temp1, temp2


ll = LinkedListMethods()
head = ll.inputLL()
ll.printLL(head)
reorderLL(head)
ll.printLL(head)