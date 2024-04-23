from LinkedList import LinkedListMethods

def reverseLinkedList(head):
    if head == None or head.next == None:
        return head
    
    prev = None
    current = head
    while(current!=None):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev # as current will be pointing at None

ll = LinkedListMethods()
head = ll.inputLL()
ll.printLL(head)
reverseHead = reverseLinkedList(head)
ll.printLL(reverseHead)
