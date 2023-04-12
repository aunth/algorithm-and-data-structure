

class Node:
    def __init__(self, value=0):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_item(self, index):
        if index >= self.length:
            return None
        item = self.head
        i = 0
        while (i < index):
            item = item.next
            i += 1
        return item.data

    def print_list(self):
        if self.length == 0:
            print("None")
            return
        head = self.head 
        print(f"{head.data} -> ", end='')
        next = head.next
        while (next != None):
            print(f"{next.data} -> ", end='')
            next = next.next
        print("None")

    def append(self, node: Node):
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
        return True
        
    def insert(self, node: Node, index: int) -> None:
        print(f"Inserting...({node.data})")
        if index < 0:
            return False
        if index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        elif index >= self.length:
            self.append(node)
        else: 
            ptr = self.head
            i = 0
            while (i < index - 1):
                ptr = ptr.next
                i += 1
            node.next = ptr.next
            ptr.next = node
            self.length += 1
        return True
        
    def delete(self, index):
        print("Deliting...")
        if self.head is None:
            return False
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            i = 1
            prev = self.head
            curr = self.head.next
            while i < index:
                prev = curr
                curr = curr.next
                i += 1
            if i == self.length - 1:
                self.tail = prev
            prev.next = curr.next
            self.length -= 1
        return True


if __name__ == "__main__":
    linked_list = LinkedList()
    
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    
    linked_list.append(a)
    linked_list.print_list()
    linked_list.insert(b, 10)
    linked_list.print_list()
    linked_list.insert(c, 0)
    linked_list.print_list()
    linked_list.insert(d, 0)
    linked_list.print_list()
    linked_list.delete(3)
    linked_list.print_list()
    u = Node("H")
    linked_list.append(u)
    linked_list.print_list()





