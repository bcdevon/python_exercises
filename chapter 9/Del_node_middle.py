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


iter = list1.head
while iter.next.value != 10:
    iter = iter.next
del_me = iter.next
iter.next = iter.next.next
del_me = None
del del_me
    
iter = list1.head
while iter is not None:
    print(iter.value)
    iter = iter.next



    
