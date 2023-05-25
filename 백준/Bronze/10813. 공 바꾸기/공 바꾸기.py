import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i for i in range(0, n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]

print(*basket[1:])