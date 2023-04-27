import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1

for num in range(2, n + 1):
    min_value = 1e9

    for i in range(1, int(math.sqrt(num)) + 1):
        min_value = min(min_value, dp[num - i ** 2])

    dp[num] = min_value + 1

print(dp[n]) 
