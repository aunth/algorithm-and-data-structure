import sorting_test


def insertion_sort(array):
	length = len(array)
	for i in range(1, length):
		key = array[i]
		j = i - 1
		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array

def main():
	sorting_test.tests(insertion_sort, 1000)

main()