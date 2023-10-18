import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def _union(a, b):
    a, b = _find(a), _find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def _find(a):
    if parent[a] == a:
        return a
    parent[a] = _find(parent[a])
    return parent[a]



for _ in range(m):
    flag, x, y = map(int,input().split())

    if flag:
        if _find(x) == _find(y):
            print("YES")
        else:
            print("NO")
    else:
        _union(x,y)