import sorting_test

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def main():
    sorting_test.tests(bubble_sort, 100)

main()
