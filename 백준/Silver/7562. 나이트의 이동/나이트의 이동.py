import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(knight_x, knight_y, final_x, final_y):
    queue = deque()
    queue.append([knight_x, knight_y])
    visited[knight_x][knight_y] = 1

    while queue:
        x, y = queue.popleft()

        if x == final_x and y == final_y:
            print(visited[x][y] - 1)
            return 
        
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

T = int(input())

for _ in range(T):
    n = int(input())
    knight_x, knight_y = map(int, input().split())
    final_x, final_y = map(int, input().split())

    visited = [[0] * n for _ in range(n)]

    bfs(knight_x, knight_y, final_x, final_y)