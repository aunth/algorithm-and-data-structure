import random

def generate_test(function_to_test, length_of_input):
	test_case = [random.randint(-1000, 1000) for _ in range(length_of_input)]
	assert function_to_test(test_case) == sorted(test_case), f"test failed\nInput: {test_case}\nOutput: {function_to_test(test_case)}"

def tests(function_to_test, number_of_test):
	for i in range(number_of_test):
		generate_test(function_to_test, 1000)