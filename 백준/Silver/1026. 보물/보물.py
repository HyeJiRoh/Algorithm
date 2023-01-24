import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().strip().split()))
brr = list(map(int, input().strip().split()))
arr.sort()
sort_brr = sorted(brr, reverse=True)
result = 0

for i in range (n):
    result += arr[i]*sort_brr[i]

print(result)