from collections import deque

n, m = map(int, input().split())

map = []

for _ in range(n):
    map.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if map[nx][ny] == "L" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                cnt = max(cnt, visited[nx][ny])

    return cnt - 1


result = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
