"""
Task 1
We have matrix(N * M) and King which stand on the point (1:1). 
Question: How much way we have that King are moved in point F(N:M)
  1 2 3 _ _ _ M
1 K _ _ _ _ _ _
2 _ _ _ _ _ _ _
3 _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
N _ _ _ _ _ _ F
Solution: 
1) First of all, we have to made a recursion condition
2) We search all way for point F(N:M). K[N][M] = K[N-1][M] + K[N][M-1], where K is a number of way in certain point
3) Further we have to define a few point for which we haven't calculated way
   Obviously its points are first column and first row for each of them number of way equal 0
   beacuse we need move only down(if column) and right on other side 
4) Beacuse in our matrix column and row which are 0 they don't have any function we can write in them 0 and made a barrier
   elements for our algoritm
"""
def king(N, M):
    matrix = [[0 for i in range(N+1)] for j in range(M+1)]
    matrix[1][1] = 1# (3)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1 and j == 1:
                continue
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]# (2)
    return matrix[N][M]

#print(king(10, 10))

"""
Taks 2: Gratest common subsequence (gcs)
We have 2 list A and B, len(A) == N, len(B) == M and we have to determine gratest common subsequence from A and B
F[i][j] len of gcs parts of A and B (A[0:i], B[0:j])
Solution:
1) First of all we need create matrix which contains in first column and first row 0(index is 0)
2) We need determine goal(цільова) function. We must understend how we can reduce our task
   Our function will be change independent of elements with index i and j
   F[i][j] equal:
   1) 1 + F[i-1][j-1] if A[i] == B[j], beacuse if last elements in two sequence equal, we can added 1 to len subsequence 
   which contain B[0:j-1] and A[0:i-1] beacuse last elements equal and we delete them and added 1
   Example: if we have to find len gcs lists [1,2,5,3,7,8] and [6,4,3,1,8]
   we can delete from lists 8 and reduce our problem and added 1 to len gcs lists [1,2,5,3,7] and [6,4,3,1]
   2) max(F[i-1][j], F[i][j-1]) beacuse we cannot delete last elements in lists beacuse they aren't equal we must consider 2 cases
   in each of them we deleted last element in lists and in the end we pick max len sequence from 2  
"""

def gcs(A, B):
    matrix = [[0] * (len(A)+1) for _ in range(len(B)+1)]
    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if A[j-1] == B[i-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1] 
            else: 
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[i][j]

#print(gcs([1,2,3,4,5,6], [0,9,8,7,1,2,3,4,5,6]))


"""
Task 3: Gratest common increasing subsequance (for one list A) gcis
Give list A len is M [a1, a2, a3, ., .,aj]. Find gcis
Solution:
F[j] is sequence [a1,a2....aj] which increase
We must find goal function
[a1, a2, a3,..., aj, ai] ми знаємо, що послідовність [a1,a2...aj] є найбільшою та зростаючою тепер ми маємо провірити чи 
входить в найбільшу підпослідовність число ai для цього у нас має виконуватися 2 умови:
1. ai > aj, щоб вона була послідовною
2. i > j щоб зберігся початковий порядок
"""

def func(A: list):
    F = [0] * (len(A) + 1) # FIXME
    for i in range(1, len(A)+1):
        m = 0
        for j in range(1, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]

print(func([1,2,4,5,4,1,3]))

# Алгоритм укладки рюкзака
# Алгоритм Левинштейна

