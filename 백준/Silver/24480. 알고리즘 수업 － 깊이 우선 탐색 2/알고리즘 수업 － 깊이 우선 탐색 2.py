import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

result = [0] * (n+1)
cnt = 1

def dfs(node):
    global cnt
    graph[node].sort(reverse = True)

    result[node] = cnt

    for idx in graph[node]:
        if result[idx] == 0:
            cnt += 1
            dfs(idx)

dfs(r)
print(*result[1:], sep = '\n')