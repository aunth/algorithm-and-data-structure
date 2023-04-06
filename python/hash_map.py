

class HashMap:
    def __init__(self, lenght):
        self.lenght = lenght
        self.data = [None] * lenght

    def hash(self, value):
        result = 0
        for i, j in enumerate(value):
            result += ord(j) * (i + 1)
        return result % self.lenght
    
    def get(self, key):
        index = self.hash(key)
        for i in self.data[index]:
            lenght = len(i)
            for j in range(lenght):
                if i[j][0] == key:
                    return i[j][1]
    
    def set(self, key, value):
        index = self.hash(key)
        if not self.data[index]:
            self.data[index] = [[key, value]]
        else:
            self.data[index].append([key, value])

    def print(self):
        print("{")
        for i in self.data:
            if not i:
                continue
            lenght = len(i)
            if lenght >= 2:
                for j in range(len(i)):
                    print(f"{i[j][0]} : {i[j][1]}", end=' ')
                    if j != lenght - 1:
                        print("->", end=' ')
                    else:
                        print("")
            else:
                print(f"{i[0][0]} : {i[0][1]}")
        print("}")
    
    def keys(self):
        result = []
        for i in self.data:
            if not i:
                continue
            lenght = len(i)
            for j in range(lenght):
                result.append(i[j][0])
        return result
    
if __name__ == "__main__":
    map = HashMap(10)
    map.set("Vlad", 17)
    map.set("Taras", 23)
    map.set("Denys", 19)
    map.set("Hello ", 0)
    map.set("Jonh", 100)
    map.print()
    print(map.keys())


