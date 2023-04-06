
class MyArray:
    def __init__(self) -> None:
        self.data = {}
        self.lenght = 0

    def append(self, value):
        self.data[self.lenght] = value
        self.lenght += 1

    def get(self, index):
        if index < self.lenght:
            return self.data[index]
        
    def pop(self):
        last_item = self.data[self.lenght - 1]
        del self.data[self.lenght - 1]
        self.lenght -= 1
        return last_item
    
    def delele(self, index):
        if index < self.lenght:
            for i in range(index, self.lenght-1):
                self.data[i] = self.data[i+1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        print(self.data)
    
    def insert(self, index, value):
        self.lenght += 1
        print(self.lenght)
        for i in range(self.lenght - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        print(self.data)

def selection_sort(array):
    lenght = len(array)
    for i in range(lenght):
        for j in range(i+1, lenght):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
    print(array)

def selection_sort_recutsion(array, start, end):
    if end == start:
        return
    for i in range(end, start, -1):
        if array[i] > array[end]:
            array[end], array[i] = array[i], array[end]
    print(array)
    return selection_sort_recutsion(array, start, end-1)


class MyStruct: #To implement data structure like dynamic arrays but which have delete/insert elements at the start in O(1) time
    def __init__(self): 
        self.left = {}
        self.right = {}
        self.lenght

    def append(self, value):
        lenght = len(value)
        for i in range(lenght//2):
            self.left[i] = value[i]
        
        for i in range(lenght//2, lenght):
            self.right[i] = value[i]


if __name__ == "__main__":
    print(selection_sort_recutsion([2, 3, 1, 5, 8, 19, 12], -1, 6))

