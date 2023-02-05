import sys
input = sys.stdin.readline

N, L = map(int, input().split())
hole = list(map(int, input().split()))
count = 1

hole.sort()

start = hole[0]

for location in hole[1:]:
    if location in range(start, start+L):
        continue
    else:
        start = location
        count += 1

print(count)