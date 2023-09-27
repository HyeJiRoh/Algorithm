import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

min_value = float("inf")
combi = []

for i in range(1, n + 1):
    combi.append(combinations(arr, i))

for i in combi:
    for j in i:
        x = 1
        y = 0
        for k in j:
            x *= k[0]
            y += k[1]
        min_value = min(min_value, abs(x - y))

print(min_value)
