

def levenshtein_distance(s1, s2): #O(m * n)
    m, n = len(s1), len(s2)
    distances = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                distances[i][j] = i + j
            if s1[i-1] == s2[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = min(distances[i-1][j], distances[i][j-1], distances[i-1][j-1]) + 1
    return distances[m][n]
