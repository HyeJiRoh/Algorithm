import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]
result = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

max_value = max(dp)

for i in range(n - 1, -1, -1):
    if dp[i] == max_value:
        result.append(arr[i])
        max_value -= 1

result.reverse()

print(*result)
