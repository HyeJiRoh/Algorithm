str1 = list(input())
str2 = list(input())

result1 = len(str1)
result2 = len(str2)

dp = [[0]*(result2 + 1) for _ in range(result1+1)]

for i in range(1, result1 + 1) :
    for j in range(1, result2 + 1) :
        if str1[i-1] == str2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])