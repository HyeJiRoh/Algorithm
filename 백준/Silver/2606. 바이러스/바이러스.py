import sys
input = sys.stdin.readline;

computer_num = int(input())
pair = int(input())

graph = [[] for _ in range(computer_num+1)]

for _ in range(pair):
    base_com, connected_com = map(int, input().split())
    graph[base_com].append(connected_com)
    graph[connected_com].append(base_com)

visited = [0 for _ in range(computer_num+1)]
cnt = 0

def dfs(start):
    global cnt
    visited[start] = 1

    for node in graph[start]:
        if visited[node] == 0:
            dfs(node)
            cnt += 1

dfs(1)
print(cnt)