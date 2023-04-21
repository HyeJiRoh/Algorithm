import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def dfs(start):
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for idx in range(n):
        if arr[idx] not in result:
            result.append(arr[idx])
            dfs(arr[idx])
            result.pop()

dfs(0)