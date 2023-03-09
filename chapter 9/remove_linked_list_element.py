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
list1.head.next.next.next = node(8)
list1.head.next.next.next.next = node(13)
list1.head.next.next.next.next.next = node(13)
list1.head.next.next.next.next.next.next = node(23)

def remove_element(head, num):
    if head.value == num:
        temp = head
        head = head.next
        temp = None
        del temp
    iter = head
    while iter.next is not None:
        if iter.next.value == num:
            del_me = iter.next
            iter.next = iter.next.next
            del_me = None
            del del_me
        elif iter.next.value != num:
            iter = iter.next

    print(head.value)
    # iter = head
    # while iter is not None:
    #     print(iter.value)
    #     iter = iter.next

remove_element(list1.head, 7)





 