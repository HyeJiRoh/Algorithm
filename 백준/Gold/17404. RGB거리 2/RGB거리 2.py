import sys

input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
result = 1e9
inf = 1e9

for i in range(3):
    dp = [[inf, inf, inf] for _ in range(N)]
    dp[0][i] = RGB[0][i]
    for j in range(1, N):
        dp[j][0] = RGB[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = RGB[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = RGB[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for k in range(3):
        if i != k:
            result = min(result, dp[-1][k])
print(result)
