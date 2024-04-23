from LinkedList import LinkedListMethods

def lengthLL(head):
    if head == None:
        return 0
    if head.next == None:
        return 1
    l = 0
    while(head!=None):
        l+=1
        head = head.next
    return l

def removeNthFromEnd(head, n):
    length = lengthLL(head)
    nodeIndexToRemove = length-n
    if nodeIndexToRemove == 0:
        return head.next
    prev=head
    for i in range(nodeIndexToRemove-1):
        prev = prev.next
        
    elementToRemove = prev.next
    prev.next = prev.next.next
    elementToRemove.next=None
    return head
def removeNthFromEnd2(head,n):
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next  # moving fast by n distance ahead of slow
    if fast == None: # it means it is the head which is n distance away from last and needs to be removed
        return head.next
    
    # Now move both slow and fast ptr by 1 place while distance of n will now alway be maintained between both slow and fast
    # as we already moved fast by n places
    while(fast.next!=None):
        slow = slow.next
        fast = fast.next
    # Now at this place slow will be pointing to one place before the element that needs to be removed
    slow.next = slow.next.next # removing the element
    return head

ll = LinkedListMethods()
head = ll.inputLL()
n=int(input())
# updated_head = removeNthFromEnd(head,n)
updated_head = removeNthFromEnd2(head,n)
ll.printLL(updated_head)

