from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
queue = deque([])
visit = [[False]*M for _ in range(N)]
result = [[-1]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        if row[j] == 2:
            queue.append((i, j))
            visit[i][j] = True
            result[i][j] = 0

        if row[j] == 0:
            result[i][j] = 0
    graph.append(row)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] == 1:
            queue.append((nx, ny))
            visit[nx][ny] = True
            result[nx][ny] = result[x][y] + 1

for row in result:
    for i in row:
        print(i, end=" ")
    print()