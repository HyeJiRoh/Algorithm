t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    total = 0

    for _ in range(n) :
        q, p = map(int, input().split())
        total += q*p
    print(total+s)