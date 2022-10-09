from traceback import print_last


class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class list:
    def __init__(self, head=None):
        self.head = head

listA = list()
listA.head = node(4)
listA.head.next = node(1)
listA.head.next.next = node(8)
listA.head.next.next.next = node(4)
listA.head.next.next.next.next = node(5)

listB = list()
listB.head = node(5)
listB.head.next = node(6)
listB.head.next.next = node(1)
listB.head.next.next.next = listA.head.next.next

iter = listB.head
while iter is not None:
    print(iter.value)
    iter = iter.next
print("")

iter = listA.head
while iter is not None:
    print(iter.value)
    iter = iter.next

NodeA = listA.head
NodeB = listB.head

while NodeA != NodeB:
    if NodeA is not None:
        NodeA = NodeA.next
    else: NodeA = listB.head

    if NodeB is not None:
        NodeB = NodeB.next
    else: NodeB = listA.head

if NodeA is None:
    print("no intersection")
elif NodeA == NodeB:
    print(f"linked lists intersect at {NodeA.value}")
