import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [0 for _ in range(0, n+1)]

for _ in range(m):
    a, b, ball = map(int, input().split())
    for i in range(a, b+1):
        basket[i] = ball

print(*basket[1:])