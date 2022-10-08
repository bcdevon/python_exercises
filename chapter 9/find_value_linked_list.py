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

def find_value(head):
    find_value = input("Enter value ")
    iter = head
    found = False
    while iter.next is not None:
        if iter.next.value == int(find_value):
            found = True
            break  
        iter = iter.next
    if found == True:
        print("value was found")
    elif found == False:
        print("value not found")

find_value(list1.head)



    