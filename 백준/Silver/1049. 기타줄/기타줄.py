import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
brr = []

for _ in range(m):
    a, b = map(int, input().split())
    arr.append(a)
    brr.append(b)

total = 0

a = min(arr)
b = min(brr)

while True:
    if n == 0:
        break

    if n >= 6:
        n -= 6
        total += min(a, b*6)

    else :
        if a > b*n:
            total += b*n
        else:
            total += a
        n -= n

print(total)