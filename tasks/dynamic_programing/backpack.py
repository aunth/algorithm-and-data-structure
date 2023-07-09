"""
Knapsack:
We have backpack which has capacity of W, we have to put in backpack elements which have maximum sum of values and sum of weights <= W
Solution: This problem is NP-complete what means that we cannot solve this faster than O(2^n), but if we add condition that 
W <= 10^6, we can solve this problem with dynamic programing O(W * N), where N is number of elements
"""


def knapsack(values, weights, W):# values and weights are lists. Value and weight of element i locate in values[i-1], weight[i-1]
    n = len(values)
    matrix = [[0 for _ in range(W+1)] for _ in range(n+1)]# create a matrix
    for i in range(1, n+1):# i respond for element
        for w in range(1, W+1):# w respond for capacity of backpack in this moment
            if weights[i-1] <= w: # if weight of this element smaller than capacity of backpack it means that we can put this element in backpack
                matrix[i][w] = max(matrix[i-1][w], values[i-1] + matrix[i-1][w-weights[i-1]]) # we decided what be better: if we don't put this element(leave value of last element) 
                # or put this element, get value of this element (value[i-1]) then add this to max value of backpack with capacity that smaller on weight of current element (matrix[i-1][w-weight[i-1]])
            else:
                matrix[i][w] = matrix[i-1][w]# we cannot put element i and we just leave max value of last element
    return matrix[n][W]