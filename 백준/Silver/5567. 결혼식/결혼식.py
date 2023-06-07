from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    visit[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in range(1, n + 1):
            if visit[i] == 0 and s[a][i] == 1:
                q.append(i)
                visit[i] = visit[a] + 1

n = int(input())
m = int(input())

s = [[0] * (n + 1) for i in range(n + 1)]

visit = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

bfs(1)

cnt = 0

for i in range(2, n + 1):
    if visit[i] < 4 and visit[i] != 0:
        cnt += 1

print(cnt)