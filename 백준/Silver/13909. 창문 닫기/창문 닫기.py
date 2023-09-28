import sys
input = sys.stdin.readline

answer = 0
n = int(input())

for num in range(1, n+1):
    if num ** 2 <= n:
        answer += 1

print(answer)