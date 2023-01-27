import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nrr = list(map(int, input().split()))
mrr = list(map(int, input().split()))
arr = list(nrr+mrr)
arr.sort()

for i in arr :
    print(i, end = " ")