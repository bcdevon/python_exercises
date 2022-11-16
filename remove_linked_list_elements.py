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

def del_nodes_value(head, value):
    iter = head
    del_node = value
    if iter == int(del_node):
        return iter
    if iter.value == int(del_node) and iter.next is None:
        del_head = head
        del_head = None
        del del_head
     
    while iter.next is not None:
        if head.value == int(del_node):
            del_head = head
            head = head.next
            del_head = None
            del del_head
        if iter.next.value == int(del_node):
            del_me = iter.next
            iter.next = iter.next.next
            del_me = None
            del del_me
            print(f"node with {value} deleted")
       
        iter = iter.next
    iter = head
    while iter is not None:
        print(iter.value)
        iter = iter.next

del_nodes_value(list1.head, 5)