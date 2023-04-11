import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        land[x][y] = 1

    visited = [[0] * m for _ in range(n)]
    result = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if land[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)