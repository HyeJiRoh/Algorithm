import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().split()))

max_len = 0
counter = [0] * (max(num) + 1)

left, right = 0, 0

while right < N:
    if counter[num[right]] < K:
        counter[num[right]] += 1
        right += 1
    else:
        counter[num[left]] -= 1
        left += 1
    max_len = max(max_len, right - left)

print(max_len)
