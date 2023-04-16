from linked_list import LinkedList, Node

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.length = 0
        self.data = []

    def peek(self):
        return self.top
    
    def push(self, value):
        self.data.append(value)
        self.top = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        removed = self.data.pop(-1)
        self.length -= 1
        if self.length > 0:
            self.top = self.data[-1]
        else:
            self.top = None
        return removed
    
    def is_empty(self):
        if self.length != 0:
            return False
        return True
    

class Stack2:
    def __init__(self) -> None:
        self.top = None
        self.data = LinkedList()
        self.length = 0

    def peek(self):
        return self.top
    
    def push(self, value):
        new_node = Node(value)
        self.data.append(new_node)
        self.length += 1
        self.top = value

    def pop(self):
        if self.length == 0:
            return None
        length_data = self.data.length
        removed = self.data.delete(length_data-1)
        self.length -= 1
        if self.length > 0:
            self.top = self.data.get_item(self.data.length - 1)
        else:
            self.top = None  
        return removed


if __name__ == "__main__":
    stack = Stack2()
    for i in range(10):
        stack.push(i)
    print(stack.peek())
    stack.data.print_list()
    value = stack.pop()
    while (value != None):
        print(value)
        value = stack.pop()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

        

    