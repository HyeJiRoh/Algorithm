import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(x, y):
    graph[x][y] = 0

    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    graph = []

    if w == 0 and h == 0:
        break

    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    island_cnt = 0

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y)
                island_cnt += 1

    print(island_cnt)
