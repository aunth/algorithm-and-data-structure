
class Graph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_vertex = {}

    def add_vertex(self, node):
        self.adjacent_vertex[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adjacent_vertex or node2 not in self.adjacent_vertex:
            return False
        self.adjacent_vertex[node1].append(node2)
        self.adjacent_vertex[node2].append(node1)
        return True

    def show_connection(self):
        for node in self.adjacent_vertex:
            connections = self.adjacent_vertex[node]
            if connections:
                print(f"{node} is connected to {connections}")

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.show_connection()

