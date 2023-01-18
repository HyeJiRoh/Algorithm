import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = {}

for _ in range(N) :
    site, password = input().split()
    arr[site] = password

for _ in range(M) :
    print(arr[input().strip()])