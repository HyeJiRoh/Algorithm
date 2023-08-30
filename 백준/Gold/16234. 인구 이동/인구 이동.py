import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, l, r = map(int,input().split())
people = []

for _ in range(n):
    people.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(a, b, graph):
    visitied[a][b] = True
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if (not visitied[nx][ny]) and (l <= (abs(graph[nx][ny] - graph[a][b])) <= r):
                check.append((nx, ny))
                dfs(nx, ny, graph)
    return check

count = 0
while True:
    visitied = [[False] * n for _ in range(n)]
    flag = False 
    for i in range(n):
        for j in range(n):
            check = [(i, j)]
            
            if not visitied[i][j]:
                check = dfs(i, j, people)            
            
            if len(check) > 1:
                flag = True
                sum = 0
                for x, y in check:
                    sum += people[x][y]
                avg = sum // len(check)
                for a, b in check:
                    people[a][b] = int(avg)

    if not flag:
        print(count)
        break
    
    count += 1