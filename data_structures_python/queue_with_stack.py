

class Stack:
    def __init__(self) -> None:
        self.data = []

    def peek(self):
        if self.data:
            return self.data[-1]
        
    def pop(self):
        if self.data:
            return self.data.pop()
        return None
    
    def push(self, item):
        self.data.append(item)

    def size(self):
        return len(self.data)
    
    def is_empty(self):
        if self.data:
            return False
        return True
    
class Queue:
    def __init__(self):
        self.data1 = Stack()
        self.data2 = Stack()

    def enqueue(self, item):
        length = self.data1.size
        for i in range(length):
            self.data1.push(self.data2.pop())
        self.data1.push(item)

    def dequeue(self):
        length = self.data1.size()
        for i in range(length):
            self.data2.push(self.data1.pop())
        removed = self.data2.pop()
        return removed
    
    def is_empty(self):
        if self.data1.is_empty():
            return True
        return False

    def peek(self):
        if self.data1.size > 0:
            return self.data1.peek()
        elif self.data2.size > 0:
            return self.data2.peek()
        else:
            return None
        

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push("Hello world")
    print("Peek : ", stack.peek())
    stack.push("None")
    print("Peek : ", stack.peek())
    print(stack.pop())
    print("Peek : ", stack.peek())
    print(stack.pop())
    print("Peek : ", stack.peek())
    print(stack.pop())
    print(stack.pop())
