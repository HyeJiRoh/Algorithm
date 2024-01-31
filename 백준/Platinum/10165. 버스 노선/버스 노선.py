import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

path1 = []
path2 = []

visited = {i: False for i in range(1, M+1)}

minA = int(1e12)
maxB = -1

for i in range(1, M+1):
    a, b = map(int, input().split())

    if a <= b:
        path1.append((a, b, i))
    else:
        minA = min(minA, a)
        maxB = max(maxB, b)
        b = b + N
        path2.append((a, b, i))
    visited[i] = True
    
path1.sort(key = lambda x : (x[0], -x[1]))
path2.sort(key = lambda x : (x[0], -x[1]))

right = 0

for i in range(len(path1)):
    if minA <= path1[i][0]:
        visited[path1[i][2]] = False
    if maxB >= path1[i][1]:
        visited[path1[i][2]] = False
    if path1[i][1] <= right:
        visited[path1[i][2]] = False
    else:
        right = path1[i][1]

right = 0
for i in range(len(path2)):
    if path2[i][1] <= right:
        visited[path2[i][2]] = False
    else:
        right = path2[i][1]
    
for i in range(1,M+1):
    if visited[i]:
        print(i, end=' ')