class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

def getDecimalValue(head):
    binary = ""
    iter = head
    while iter is not None:
        binary += str(iter.val)
        iter = iter.next
    num = int(binary,2)
    print(num)
getDecimalValue(head)