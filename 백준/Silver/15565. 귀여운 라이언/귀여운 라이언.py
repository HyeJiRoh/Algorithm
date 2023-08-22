import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

min_len = int(1e6)
cnt = 0
left, right = 0, 0

if dolls[right] == 1:
    cnt += 1

while right < N:
    if cnt == K:
        min_len = min(min_len, right - left + 1)
        if dolls[left] == 1:
            cnt -= 1
        left += 1
    else:
        right += 1
        if right < N and dolls[right] == 1:
            cnt += 1

if min_len == int(1e6):
    print(-1)
else:
    print(min_len)
