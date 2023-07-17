import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
temp = [0]
result = 0

for i in range(n):
    result += numbers[i]
    temp.append(result)

for i in range(m):
    i, j = map(int, input().split())
    print(temp[j] - temp[i - 1])