import sorting_test

def quick_sort(array):
	if len(array) <= 1:
		return array
	pivot = array[0]
	less = [i for i in array[1:] if i <= pivot]
	grater = [i for i in array[1:] if i > pivot]
	return quick_sort(less) + [pivot] + quick_sort(grater)

def main():
	sorting_test.tests(quick_sort, 1000)

main()