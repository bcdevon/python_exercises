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

def del_node_middle(head):
    del_node = input("enter node to delete ")
    iter = head
    found = False
    while iter.next is not None:
        if iter.next.value == int(del_node):
            found = True
            break
        iter = iter.next
    if found == True:
        del_me = iter.next
        iter.next = iter.next.next
        del_me = None
        del del_me
        print("node deleted")
    elif found == False:
        print("value not in linked list")
    
    iter = head
    while iter is not None:
        print(iter.value)
        iter = iter.next

iter = list1.head
while iter is not None:
    print(iter.value)
    iter = iter.next

del_node_middle(list1.head)



    
