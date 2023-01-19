import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

for i in arr :
    print(i, end=" ")