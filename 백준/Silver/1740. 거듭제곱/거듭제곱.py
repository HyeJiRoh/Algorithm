import sys
input = sys.stdin.readline

n = int(input())
arr = []
num = 0

while n > 0:
    arr.append(n % 2)
    n //= 2

for idx in range(len(arr)):
    if arr[idx] == 1:
        num += 3 ** idx
print(num)