import sys
input = sys.stdin.readline

n = int(input())
m = []

for _ in range(n):
    m.append(int(input()))

m.sort(reverse=True)
result = []

for i in range(n):
    result.append(m[i]*(i+1))

print(max(result))