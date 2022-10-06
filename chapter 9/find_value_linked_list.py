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
while iter is not None:
    if iter.value == 13:
        print(f"{iter.value} is in the linked list")
    elif iter.next is None:
        print("value not found")
    iter = iter.next
    
    