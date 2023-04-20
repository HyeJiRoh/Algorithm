import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for idx in range(start, n + 1):
        result.append(idx)
        dfs(idx)
        result.pop()

dfs(1)