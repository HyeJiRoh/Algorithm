import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = (max(dp[i], dp[i] + dp[i - 1]))

print(max(dp))