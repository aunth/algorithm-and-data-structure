import random


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def generate_test(length_of_input):
	test_case = [random.randint(-1000, 1000) for _ in range(length_of_input)]
	assert bubble_sort(test_case) == sorted(test_case), f"test failed\nInput: {test_case}\nOutput: {bubble_sort(test_case)}"

def tests():
	for i in range(1, 1000):
		generate_test(i)

def main():
    tests()
    
main()
