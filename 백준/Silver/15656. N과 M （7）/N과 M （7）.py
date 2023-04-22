import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

arr.sort()

def dfs(node):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for idx in arr:
        result.append(idx)
        dfs(idx)
        result.pop()

dfs(0)