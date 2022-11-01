class linked_list_node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linked_list_node(value) #insert values into linked list
        if self.head is None:           # check if linked list has any nodes
            self.head = node            #if the head is none the head is now equal to the node we created
            return
        
        current_Node = self.head
        while True:
            if current_Node.nextNode is None: #looks for the tail or last node
                current_Node.nextNode = node  #make the next node our node
                break
            current_Node = current_Node.nextNode #if its not the tail kep traversing through linked list to find tail
    
    def print_linked_list(self):
        current_Node = self.head
        while current_Node is not None:
            print(current_Node.value, "-> ", end="") # end="" makes it print on one line
            current_Node = current_Node.nextNode
        print("None")

list1 = linked_list()
list1.head = linked_list_node("Monday")
nextDay1 = linked_list_node("Tuesday")
nextDay2 = linked_list_node("Wednesday")
list1.head.nextNode = nextDay1
nextDay1.nextNode = nextDay2

list1.print_linked_list()

# ll = linked_list()
# ll.print_linked_list()
# ll.insert("3")
# ll.print_linked_list()
# ll.insert("44")
# ll.print_linked_list()
# ll.insert("55")
# ll.print_linked_list()
