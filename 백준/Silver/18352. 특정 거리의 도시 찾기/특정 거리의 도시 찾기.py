from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n + 1)
visited[x] = 0

q = deque()
q.append(x)

while q:
    now = q.popleft()

    for next in graph[now]:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)

flag = False

for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)
