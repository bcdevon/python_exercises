class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    iter = head
    while iter is not None:
        print(iter.value, '=> ',end='')
        iter = iter.next
    print("")
    
head = node(7)
head.next = node(11)
head.next.next = node(3)

print_linked_list(head)
last = None
middle = head
first = head

while middle is not None and first is not None:
    first = middle.next
    middle.next = last
    last = middle
    middle = first

head = last

print_linked_list(head)


    
