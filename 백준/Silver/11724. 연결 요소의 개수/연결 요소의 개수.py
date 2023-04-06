import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

cnt = 0
visited = [0] * (n+1)

def bfs(start_node):
    visited[start_node] = 1

    for check in graph[start_node]:
        if visited[check] == 0:
            bfs(check)

for idx in range(1, n+1):
    if visited[idx] == 0:
        bfs(idx)
        cnt += 1

print(cnt)