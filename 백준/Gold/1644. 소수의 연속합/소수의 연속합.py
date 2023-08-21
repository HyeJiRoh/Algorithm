import sys

input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input())
arr = []
total = 0

if num == 1:
    print(0)
    exit(0)

for i in range(2, num + 1):
    if is_prime(i):
        arr.append(i)

left = 0
right = 0
total = arr[0]
cnt = 0

while left <= right:
    if total > num:
        total -= arr[left]
        left += 1
    else:
        if total == num:
            cnt += 1
        right += 1
        if right == len(arr):
            break
        total += arr[right]

print(cnt)
