import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

for i in range(N):
    tmp = num[:i] + num[i + 1 :]
    left, right = 0, len(tmp) - 1

    while left < right:
        total = tmp[left] + tmp[right]

        if total == num[i]:
            cnt += 1
            break
        if total < num[i]:
            left += 1
        else:
            right -= 1

print(cnt)
