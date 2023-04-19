import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

def dfs(a):
    for idx in graph[a]:
        if visited[idx] == 0:
            visited[idx] = visited[a] + 1
            dfs(idx)

dfs(a)

print(visited[b] if visited[b] > 0 else -1)