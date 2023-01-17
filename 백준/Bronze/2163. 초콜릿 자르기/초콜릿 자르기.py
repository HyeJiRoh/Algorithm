import sys
input = sys.stdin.readline

N, M = map(int, input().split())
max = max(N,M)
min = min(N,M)
max_count = 0
min_count = 0

for i in range(max, 1, -1) :
    max_count += 1

for i in range(min, 1, -1) :
    min_count += 1

print(min_count + max_count*min)