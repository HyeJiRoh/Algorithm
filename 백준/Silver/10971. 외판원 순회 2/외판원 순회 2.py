n = int(input())
world = []

for _ in range(n):
    world.append(list(map(int, input().split())))

visited = [0] * n
base = 123456789

check = 0


def dfs(f, check, visited):
    global base

    if check > base:
        return

    if sum(visited) == n - 1:
        if world[f][0]:
            base = min(base, check + world[f][0])
        return

    for i in range(1, n):
        if world[f][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i, check + world[f][i], visited)
            visited[i] = 0


for i in range(1, n):
    if world[0][i]:
        visited[i] = 1
        dfs(i, world[0][i], visited)
        visited[i] = 0

print(base)