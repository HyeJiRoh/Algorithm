from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = [0] * (n + 1)
cnt = 1

def bfs(node):
    global cnt
    queue = deque([node])
    visited[node] = cnt

    while queue:
        v = queue.popleft()
        graph[v].sort(reverse = True)

        for i in graph[v]:
            if visited[i] == 0:
                cnt +=1
                queue.append(i)
                visited[i] += cnt

bfs(r)

for i in range(1, n + 1):
    print(visited[i])