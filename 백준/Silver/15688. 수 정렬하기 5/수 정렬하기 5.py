import sys
input = sys.stdin.readline

n = int(input())

result = []

for _ in range(n):
    result.append(int(input()))

result.sort()

print(*result, sep = "\n")