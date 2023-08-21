import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
total = arr[0]
length = sys.maxsize

while True:
    if total >= s:
        length = min(length, right - left + 1)
        total -= arr[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        total += arr[right]

if length == sys.maxsize:
    print(0)
else:
    print(length)
