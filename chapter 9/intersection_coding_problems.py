class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_intersection_of_two_linked_lists(head_a, head_b):
    linked_listA = list()

    iter = head_a