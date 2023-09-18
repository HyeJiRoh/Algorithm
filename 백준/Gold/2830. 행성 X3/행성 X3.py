import sys

input = sys.stdin.readline

n = int(input())
name = [int(input()) for i in range(n)]

D = [0] * 30

for i in name:
    k = i
    cnt = 0
    
    while k > 0:
        D[cnt] += k % 2
        k //= 2
        cnt += 1
answer = 0
c = 1

for i in D:
    answer += c * (i * (n - i))
    c *= 2

print(answer)
