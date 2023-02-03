import sys
input = sys.stdin.readline

i = 0
while True:
    l, p, v = map(int, input().split())
    i += 1
    result = 0

    if l == p == v ==0:
        break

    result = (v//p)*l + min(v%p, l)
    print("Case %d: %d"%(i, result))