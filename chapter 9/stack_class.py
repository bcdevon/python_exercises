class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) -1]

new_stack = Stack()
new_stack.push(5)
new_stack.push(11)

print(new_stack.peek())

