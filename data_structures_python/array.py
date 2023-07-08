
class MyArray:
    def __init__(self) -> None:
        self.data = {}
        self.length = 0

    def append(self, value):
        self.data[self.length] = value
        self.length += 1

    def get(self, index):
        if index < self.length:
            return self.data[index]
        
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delele(self, index):
        if index < self.length:
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        print(self.data)
    
    def insert(self, index, value):
        self.length += 1
        print(self.length)
        print(self.data)
        print(index)
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        print(self.data)

    def print_array(self):
        print("[ ", end='')
        for i in range(self.length-1):
            print(f"{self.data[i]}, ", end='')
        print(f"{self.data[self.length-1]} ]")


if __name__ == "__main__":
    a = MyArray()
    a.append(10)
    a.append("Value")
    a.insert(1, "hello world")
    a.insert(1, "50")
    a.print_array()

