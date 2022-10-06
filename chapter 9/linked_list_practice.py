from ast import Delete


class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head = node(5)
head.next = node(2)
head.next.next = node(7)

iter = head
while iter is not None:
    print(iter.value)
    iter = iter.next

iter = head
while iter.next is not None:
    iter = iter.next
iter.next = node(9)


# iter = head
# while iter.next.value != 9:
#     iter = iter.next
# del_me = iter.next
# iter.next = None
# del del_me 

# iter = head
# while iter is not None:
#     print(iter.value)
#     iter = iter.next


