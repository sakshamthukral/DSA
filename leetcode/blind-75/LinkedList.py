class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
class LinkedListMethods:
    def __init__(self):
        self.head = None
    def inputLL(self):
        listInput = [int(ele) for ele in input().split()]
        head = None
        tail = None
        for data in listInput:
            if data == -1:
                break
            newnode = ListNode(data)
            if head==None and tail == None:
                head = newnode
                tail = newnode
            else:
                tail.next=newnode
                tail = newnode
        return head
    
    def printLL(self,head):
        if head == None:
            print('None')
            return
        temp = head
        while(temp.next!=None):
            print(temp.val,end="->")
            temp = temp.next
        print(temp.val)


