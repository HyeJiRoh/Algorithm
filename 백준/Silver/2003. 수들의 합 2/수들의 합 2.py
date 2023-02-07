import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
count = 0

while right<=n and left<=right:
    num = arr[left:right]
    total = sum(num)

    if total == m:
        count += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(count)