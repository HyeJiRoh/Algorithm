import sys
input = sys.stdin.readline
from collections import deque

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    
    for i in range(1, n + 1):
        if visit[i] == 0 and arr[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0

    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]

        for i in range(1, n + 1):
            if visit[i] == 1 and arr[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())

arr = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

dfs(v)
print()
bfs(v)