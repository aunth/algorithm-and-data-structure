"""
Task: An increasing subarray of an integer array is any consecutive sequence of array integers whose
values strictly increase. Write Python function count_long_subarrays(A) which accepts Python Tuple 
A = (a0, a1, . . . , an−1) of n > 0 positive integers, and returns the number of longest increasing 
subarrays of A, i.e., the number of increasing subarrays with length at least as large as every other increasing 
subarray. For example, if A = (1,3,4,2,7,5,6,9,8), your program should return 2 since the maximum length 
of any increasing subarray of A is three and there are two increasing subarrays with that length: specifically, 
subarrays (1,3,4) and (5,6,9).
"""

# def count_long_subarrays(A):
#     len_array = len(A)
#     lenght = 0
#     max_array_len = 0
#     for i in range(len_array-1):
#         current_lenght = 0
#         for j in range(i+1, len_array):
#             if A[j] > A[j-1]:
#                 current_lenght+=1
#             else:
#                 break
#         print(f"from {i} to {j} {current_lenght}")
#         if max_array_len < current_lenght:
#             max_array_len = current_lenght
#             lenght = 1
#         elif max_array_len == current_lenght:
#             lenght+=1
#     print(lenght)

# def gpt_version(A):
#     n = len(A)
#     dp = [1] * n
#     for i in range(1, n):
#         if A[i] > A[i-1]:
#             dp[i] = dp[i-1] + 1
#     max_len = max(dp)
#     count = dp.count(max_len)
#     print(count)
# A = (1,3,4,2,7,5,6,9,5,6)
# gpt_version(A)


def all_pairs(A):
    for i in A:
        for j in A:
            print(f"[{i}, {j}]")
    return None

all_pairs([1, 2, 3, 4, 5])



            
