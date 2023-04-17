import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = [0 for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]

def dfs(node):
    visited[node] = 1

    for idx in graph[node]:
        if visited[idx] == False:
            result[idx] = node
            dfs(idx)

dfs(1)
print(*result[2:], sep = '\n')