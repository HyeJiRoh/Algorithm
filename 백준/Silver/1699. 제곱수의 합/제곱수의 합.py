import sys
input = sys.stdin.readline

n = int(input())
    
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = i

    for j in range(1, i):
        
        if(j**2) > i:
            break
        
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1

print(dp[n])