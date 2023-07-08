from linked_list import LinkedList, Node

class Queue:
    def __init__(self):
        self.data = LinkedList()
        self.first = None
        self.length = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.length == 0:
            self.first = new_node
        self.data.insert(new_node, self.length)
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            removed = self.data.delete(0)
            self.length -= 1
            if self.length > 0:
                self.first = self.first.next 
            else:
                self.first = None
            return removed
        return None

    def peek(self):
        return self.first
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False
    

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")
    print("Peek: ", queue.peek().data)
    queue.data.print_list()
    print(queue.is_empty())
    print(queue.dequeue())
    queue.data.print_list()
    print(queue.is_empty())
    print(queue.dequeue())
    queue.data.print_list()
    print(queue.is_empty())
    print(queue.dequeue())
    queue.data.print_list()
    print(queue.is_empty())





