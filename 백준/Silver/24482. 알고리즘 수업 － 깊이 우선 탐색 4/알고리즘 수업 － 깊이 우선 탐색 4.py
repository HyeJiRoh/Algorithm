import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

result = [-1] * (n+1)

def dfs(node):
    graph[node].sort(reverse = True)

    for idx in graph[node]:
        if result[idx] == -1:
            result[idx] = result[node] + 1
            dfs(idx)

result[r] = 0

dfs(r)
print(*result[1:], sep = '\n')
