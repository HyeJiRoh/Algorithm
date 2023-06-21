N = int(input())
n = N + 2
ans = 1 * n

for i in range(2, N+1):
    ans += i * n
    
print(ans)