import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]

for i in range(n):
    map = input().strip()
    for j, k in enumerate(map):
        graph[i][j] = int(k)

visited = [[0] * n for _ in range(n)]
check = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global check
    visited[x][y] = '1'

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == 1:
        check += 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0  or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

result = [] 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            result.append(check)
            check = 0

result.sort()

print(len(result))
print(*result, sep = '\n')