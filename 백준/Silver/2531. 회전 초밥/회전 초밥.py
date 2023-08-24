import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []

for _ in range(N):
    sushi.append(int(input()))
sushi.extend(sushi)

tmp = []
left, right = 0, 0
result = 0
tmp = defaultdict(int)

while right < k:
    tmp[sushi[right]] += 1
    right += 1

tmp[c] += 1

while right < len(sushi):
    result = max(result, len(tmp))
    tmp[sushi[left]] -= 1

    if tmp[sushi[left]] == 0:
        del tmp[sushi[left]]

    tmp[sushi[right]] += 1
    left += 1
    right += 1

print(result)
