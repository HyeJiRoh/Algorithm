from collections import deque

n, m, k = map(int, input().split())

trash = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    trash[r - 1][c - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    size = 1
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if trash[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    size += 1
    return size


result = 0

for i in range(n):
    for j in range(m):
        if trash[i][j] == 1 and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)
