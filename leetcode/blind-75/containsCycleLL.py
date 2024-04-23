from LinkedList import LinkedListMethods

# Algorithm: Floyde's tortoise and hare algorithm
def containsCycle(head): 
    tortoise = head
    hare = head
    while(hare!=None and hare.next!=None):
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise==hare:
            return True
    return False

ll = LinkedListMethods()
head = ll.inputLL()
print(containsCycle(head))