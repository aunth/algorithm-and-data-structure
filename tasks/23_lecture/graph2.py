

class Stack:
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)

    def pop(self):
        try:
            result = self.values[0]
        except IndexError:
            return None
        else:
            self.values = self.values[1:]
        return result


def main(edge, graph):
    stack = Stack()
    checked_edges = set()
    colours_of_edges = {i: None for i in graph}
    stack.add(edge)
    while True:
        next = stack.pop()
        if next == None:
            break
        else:
            if next not in checked_edges:
                if all_white_neighbors(next, graph, colours_of_edges):
                    colours_of_edges[next] = "black"
                    print(f"Painted {next} to black")
                else:
                    colours_of_edges[next] = "white"
                    print(f"Painted {next} to white")
                for i in graph[next]:
                    stack.add(i)
                checked_edges.add(next)
            else:
                next = stack.pop()
    return len([i for i in colours_of_edges if colours_of_edges[i] == "black"])

def all_white_neighbors(edges, graph, color):
    return all(color[j] != "black" for j in graph[edges])



def load_graph():
    result = {}
    while True:
        string = input()
        if string == "end":
            break
        v1, v2 = string.split()
        for i, j in [(v1, v2), (v2, v1)]:
            if i not in result:
                result[i] = {j}
            else:
                result[i].add(j)
    return result
        


graph = load_graph()
for i in graph:
    print(f"We started with {i} and we painted {main(i, graph)}")
    


