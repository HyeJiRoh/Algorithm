import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = list(input().split())
brr = list(input().split())

result = set(arr)^set(brr)
print(len(result))