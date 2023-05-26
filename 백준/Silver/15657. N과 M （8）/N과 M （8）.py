import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

arr.sort()

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for idx in range(start, n):
        result.append(arr[idx])
        dfs(idx)
        result.pop()

dfs(0)