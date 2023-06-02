import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]

max_width = min(n, m)
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(max_width):
            if (i+k) < n and (j+k) < m and (board[i][j] == board[i+k][j] == board[i][j+k] == board[i+k][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)