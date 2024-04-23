from LinkedList import LinkedListMethods

def mergeKSortedLists(lists):
    if len(lists) == 0:
        return None
    while len(lists)>1:
        mergedLists = []
        for i in range(0,len(lists),2):
            list1 = lists[i]
            list2 = lists[i+1] if i+1<len(lists) else None
            mergeResult = mergeSortedLists(list1,list2)
            mergedLists.append(mergeResult)
        lists = mergedLists
    return lists[0]


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
k = int(input())
lists = []
while(k>0):
    head = ll.inputLL()
    lists.append(head)
    k-=1
mergedSortedHead = mergeKSortedLists(lists)
ll.printLL(mergedSortedHead)