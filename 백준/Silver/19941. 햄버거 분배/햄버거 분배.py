import sys
input = sys.stdin.readline

N,K = map(int, input().split())
s = list(input())
 
count = 0

for i in range(N):
    if s[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and s[j] == 'H':
                count += 1
                s[j] = 'X'
                break
 
print(count)