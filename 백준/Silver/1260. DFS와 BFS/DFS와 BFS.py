from collections import deque
import sys
input = sys.stdin.readline

def dfs(node):
    print(node, end = ' ')
    visited[node] = True

    for idx in graph[node]:
        if not(visited[idx]):
            dfs(idx)

def bfs(node):
    queue = deque([node])

    while queue:
        node = queue.popleft()

        if visited[node] == False:
            visited[node] = True
            print(node, end = ' ')

            for idx in graph[node]:
                if not(visited[idx]):
                    queue.append(idx)

n, m, v = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

for idx in graph:
    idx.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)