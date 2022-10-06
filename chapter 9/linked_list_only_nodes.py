# nodes
# 1. value - anything strings, integers, objects
# 2. The next Node

class Linked_List_Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# "3" -> "7" -> "10"

node1 = Linked_List_Node("3") # "3"
node2 = Linked_List_Node("7") # "7"
node3 = Linked_List_Node("10") # "10"
node4 = Linked_List_Node("77")

node1.nextNode = node2 # node1 -> node2, "3" -> "7"
node2.nextNode = node3 # node2 -> node3, "7" -> "10"
node3.nextNode = node4

current_Node = node1
while True:
    print(current_Node.value, "-> ", end="") #end="" makes it all print on one line
    if current_Node.nextNode is None:
        print("None")
        break
    current_Node = current_Node.nextNode


    
