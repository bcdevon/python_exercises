from ast import Delete


class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class list:
    def __init__(self, head=None):
        self.head = head


list1 = list()
list1.head = node(7)
list1.head.next = node(8)
list1.head.next.next = node(10)
list1.head.next.next.next = node(13)

temp = list1.head
head = list1.head.next
temp = None
del temp
        
iter = head
while iter is not None:
    print(iter.value)
    iter = iter.next






 