import sys

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == people[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(*result)
