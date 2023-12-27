n = int(input())
x = []
y = []
result = [-1] * n

for _ in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

for i in x:
    for j in y:
        dist = []
        for k in range(n):
            dist.append(abs(x[k] - i) + abs(y[k] - j))

        dist.sort()

        tmp = 0
        for l in range(len(dist)):
            d = dist[l]
            tmp += d
            if result[l] == -1:
                result[l] = tmp
            else:
                result[l] = min(tmp, result[l])

print(*result)