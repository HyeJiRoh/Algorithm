from collections import deque

n = int(input())

graph = []
maxHeight = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxHeight:
            maxHeight = graph[i][j]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, height, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > height and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


result = 0

for height in range(maxHeight):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and visited[i][j] == 0:
                bfs(i, j, height, visited)
                cnt += 1

        if result < cnt:
            result = cnt

print(result)
