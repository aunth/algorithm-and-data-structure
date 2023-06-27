from collections import deque


def breadth_first_search(graph, start):
	visited = set()
	queue = deque([start])
	
	while (queue):
		vertex = queue.popleft()
		if vertex not in visited:
			visited.add(vertex)
			print(vertex)
			for neighbor in graph[vertex]:
				if neighbor not in visited:
					queue.append(neighbor)

def main():
	graph = {
	    'A': ['B', 'C'],
	    'B': ['A', 'D', 'E'],
	    'C': ['A', 'F'],
	    'D': ['B'],
	    'E': ['B', 'F'],
	    'F': ['C', 'E']
	}

	breadth_first_search(graph, 'A')

main()