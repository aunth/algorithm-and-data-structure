def sum_func(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_func(arr[1:])

def count_elem(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_elem(arr[1:])

def binary_search(arr, n, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if n == arr[mid]:
            return mid
        elif arr[mid] > n:
            binary_search(arr, n, low, mid-1)
        else:
            binary_search(arr, n, mid+1, high)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        main = arr[0]
        left, right = [], []
        for i in arr[1:]:
            if i > main:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [main] + quick_sort(right)


print(quick_sort([2,1,4,5,3,7,9]))
        
    