import sys
import sorting_test
sys.path.insert(0, '/Users/vladmaslianko/programing/algoritm and data structures /python')

import heap as hp

a = [1, 6, 3, 1, 2, 9, 2]

def heap_sort(a):
	result = []
	heap = []
	lenght = len(a)
	for i in range(lenght):
		hp.insert(heap, a[i])
	for i in range(lenght):
		result.append(hp.remove_min(heap))
	return result

def main():
	sorting_test.tests(heap_sort, 10000)

if __name__ == "__main__":
	main()