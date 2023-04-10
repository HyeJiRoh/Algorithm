from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = [-1] * (n+1)

def bfs(node):
    queue = deque([node])
    visited[node] = 0

    while queue:
        node = queue.popleft()
        graph[node].sort()

        for idx in graph[node]:
            if visited[idx] == -1:
                visited[idx] = visited[node] + 1
                queue.append(idx)

bfs(r)
print(*visited[1:], sep = '\n')