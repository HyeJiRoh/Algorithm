import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []

for _ in range(n):
    result.append(list(map(int, input().split())))


result.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
    if result[i][0] == k:
        index = i
        
for i in range(n):
    if result[index][1:] == result[i][1:]:
        print(i + 1)
        break