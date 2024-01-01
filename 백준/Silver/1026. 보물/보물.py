import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr.sort()
brr.sort(reverse=True)

total = 0

for i in range(n):
    total += (arr[i] * brr[i])

print(total)