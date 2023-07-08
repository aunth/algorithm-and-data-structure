
### Binary Heap implementation with list


def swap(heap, i, j):
	heap[i], heap[j] = heap[j], heap[i]

def insert(heap, x): # O(log(n))
	max_index = len(heap) - 1
	heap.append(x)
	max_index += 1
	i = max_index
	while i > 0:
		if heap[i] < heap[(i-1)//2]:
			swap(heap, i, (i-1)//2)
			i = (i-1)//2
		else:
			break

def remove_min(heap): # O(log(n))
	size = len(heap)
	res = heap[0]
	size -= 1
	heap[0] = heap[size]
	del heap[-1]
	i = 0
	while True:
		j = i
		if 2*i + 1 < size and heap[2*i + 1] < heap[j]:
			j = 2*i + 1
		if 2*i + 2 < size and heap[2*i + 2] < heap[j]:
			j = 2*i + 2
		if i == j:
			break
		swap(heap, i, j)
		i = j
	return res


if __name__ == "__main__":
	heap = [3, 7, 5, 8, 11, 10, 13, 14, 27, 18, 38] 

	print(heap)
	print(remove_min(heap))
	print(heap)



