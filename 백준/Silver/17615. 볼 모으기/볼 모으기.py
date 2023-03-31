import sys
input = sys.stdin.readline

n = int(input())
balls = list(input().strip())

cnt = 0

for i in range(n-1, -1, -1):
    if balls[i] == balls[i-1]:
        cnt += 1
    else:
        break

balls = balls[0:n-cnt-1]

Rcnt = balls.count("R")
Bcnt = balls.count("B")

print(min(Rcnt, Bcnt))