#Task 1
# Exercise about grig which stand in point 1 and he need to get to point N.He have steps (+1 or +2). 
# How much he have different ways
# Solution:
# We known that in point N we can to get to on N-1 point and N-2 point. So we get a recursive formula K[N] = K[N-1] + K[N-2]
def traj_num(N):
    K = [0, 1] + [0] * (N-1)
    for i in range(2, N+1):
        K[i] = K[i-1] + K[i-2]

a = 10
b = 200
# Task 2
# We made task harder and added point in which you cannot get to and we added step +3
# Solution:
# Recursive formula doesn't change but we added step +3:  K[N] = K[N-1] + K[n-2] + K[n-3]
def traj_num_2(N, allowed: list): # allowed is a list in which on each point equal True if is allowed and False on other side
    K = [0, 1] + [0] * (N-1)
    for i in range(2, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]


# Task 3
# We need get to point N with min cost, we have step +1 and step +2
# In this task we get as a parametr of function list price which have price of visiting for each point
# Solution:
# Solution will be similar as other task. We must calculated by hand first two number 
# C[1] = price[1] and C[2] = price[1] + price[2] beacuse in point 2 we can get to only from point 1s 
# We know that we can get to point N on N-1 and N-2 but in this situation
# we must calculated min cost of N-1 and N-2 and added to cost visiting of point N
# We get formula: C[N] = min(C[N-1], C[N-2]) + price[i]
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




      
