from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = []
result = []
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(str, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    visited[x][y] = 1

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = 1
                queue.append((nx, ny))

red = 0
blue = 0
green = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, graph[i][j])
            
            if graph[i][j] == "R":
                red += 1
            elif graph[i][j] == "B":
                blue += 1
            elif graph[i][j] == "G":
                green += 1

rgb_total = red + blue + green

visited = [[0] * n for _ in range(n)]

red = 0
blue = 0
green = 0

for i in range(n):
    for j in range(n): 
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            if graph[i][j] == "R":
                red += 1
            elif graph[i][j] == "B":
                blue += 1

rg_total = red + blue

print(rgb_total, rg_total)