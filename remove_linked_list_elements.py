from ast import Delete


class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class list:
    def __init__(self, head=None):
        self.head = head

list1 = list()
list1.head = node(13)
list1.head.next = node(3)
list1.head.next.next = node(13)
list1.head.next.next.next = node(9)
list1.head.next.next.next.next = node(5)
list1.head.next.next.next.next.next = node(2)

def del_nodes_value(head, num):
    if head.value == int(num):
        del_head = head
        head = head.next
        del_head = None
        del del_head
    iter = head   
    while iter.next is not None:
        if iter.next.value == int(num):
            del_me = iter.next
            iter.next = iter.next.next
            del_me = None
            del del_me
            print(f"node with {num} deleted")
        iter = iter.next
    # if iter.value == int(num) and iter.next is None:
    #     del_tail = iter
    #     del_tail = None
    #     del del_tail
    iter = head
    while iter is not None:
        print(iter.value)
        iter = iter.next

del_nodes_value(list1.head, 2)