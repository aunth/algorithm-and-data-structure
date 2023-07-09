
"""
Task 1
Exercise about grig which stand in point 1 and he need to get to point N.He have steps (+1 or +2). 
How much he have different ways
Solution:
We known that in point N we can to get to on N-1 point and N-2 point. So we get a recursive formula K[N] = K[N-1] + K[N-2]
"""

def traj_num(N):
    K = [1, 1] + [0] * (N - 1)
    for i in range(2, N+1):
        K[i] = K[i-1] + K[i-2]
    return K[N]

"""
Task 2
We made task harder and added point in which you cannot get to and we added step +3
Solution:
Recursive formula doesn't change but we added step +3:  K[N] = K[N-1] + K[n-2] + K[n-3]
"""

def traj_num_2(N, allowed: list): # allowed is a list in which on each point equal True if is allowed and False on other side
    K = [1, 1, 2] + [0] * (N-2)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]

"""
Task 3
We have the same grig, but now he can jump from 1 to K steps in time. We have to count all way from 1 to N
Solution:
Idea still the same but now because of number of steps can be big we have to write second while loop
"""
def traj_num_3(N, K): 
    ways = [0] * (N + 1)
    ways[0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if i - j >= 0:
                ways[i] += ways[i - j]
    return ways[N]
"""
This algorithm run O(N * K) time. We can rewrite it to run O(N) time
"""


def traj_num_3(N, K):
    ways = [0] * (N + 1)
    ways[0] = 1
    window_sum = 1

    for i in range(1, N + 1):
        if i - K - 1 >= 0:
            window_sum -= ways[i - K - 1]
        ways[i] = window_sum
        window_sum += ways[i]

    return ways[N]

"""
 Task 4
 We need get to point N with min cost, we have step +1 and step +2
 In this task we get as a parametr of function list price which have price of visiting for each point
 Solution:
 Solution will be similar as other task. We must calculated by hand first two number 
 C[1] = price[1] and C[2] = price[1] + price[2] beacuse in point 2 we can get to only from point 1s 
 We know that we can get to point N on N-1 and N-2 but in this situation
 we must calculated min cost of N-1 and N-2 and added to cost visiting of point N
 We get formula: C[N] = min(C[N-1], C[N-2]) + price[i]
"""

def min_cost_way(N, price: list):
    C = [float("-inf", price[1], price[1] + price[2])] # C is a list which contains min cost visiting of each point
    for i in range(3, N+1):
        C[i] = min(C[i-1], C[i-2]) + price[i]
    #return C[N]
    path = [N]
    last_index = N
    while last_index != 1:
        if C[last_index] == C[last_index-1] + price[last_index]:
            last_index -= 1
        else:
            last_index -= 2
        path.append(last_index)
    return path[::-1]

"""
Task 4
We have the same grig and task is to count all ways from 0 to N but now if grig jump on k steps
next time he should jump on >= k steps.
"""
def count_ways(N, K):
    ways = [[0] * (K + 1) for _ in range(N + 1)]
    ways[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(1, j + 1):
                if i - k >= 0:
                    ways[i][j] += ways[i - k][k]

    return ways[N][K]
