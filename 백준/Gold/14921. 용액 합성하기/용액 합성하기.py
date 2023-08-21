import sys

input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left = 0
right = N - 1

result = liquids[left] + liquids[right]

while left < right:
    total = liquids[left] + liquids[right]

    if abs(total) < abs(result):
        result = total

    if total < 0:
        left += 1
    else:
        right -= 1

print(result)
