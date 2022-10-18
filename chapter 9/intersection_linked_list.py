

class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head_a = node(4)
head_a.next = node(1)
head_a.next.next = node(8)
head_a.next.next.next = node(4)
head_a.next.next.next.next = node(5)


head_b = node(5)
head_b.next = node(6)
head_b.next.next = node(1)
head_b.next.next.next = head_a.next.next

def get_intersection(head_a, head_b):
    NodeA = head_a
    NodeB = head_b

    while NodeA != NodeB:
        if NodeA is not None:
            NodeA = NodeA.next
        else: NodeA = head_b

        if NodeB is not None:
            NodeB = NodeB.next
        else: NodeB = head_a

    if NodeA is None:
        print("no intersection")
    elif NodeA == NodeB:
        print(f"linked lists intersect at {NodeA.value}")

get_intersection(head_a, head_b)
