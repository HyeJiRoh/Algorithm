n = int(input())
brackets = list(input().split())
visited = [0] * 10
ans = []

def check_up(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(iter, temp):
    if iter == n + 1:
        ans.append(temp)
        return

    for i in range(10):
        if not visited[i]:
            if iter == 0 or check_up(temp[-1], str(i), brackets[iter - 1]):
                visited[i] = 1
                dfs(iter + 1, temp + str(i))
                visited[i] = 0
dfs(0, "")

print(ans[-1])
print(ans[0])