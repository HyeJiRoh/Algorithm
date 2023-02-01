import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    new = []

    for i in range(N):
        score, rank = map(int, input().split())
        new.append((score, rank))
    new.sort(key=lambda doc:doc[0])
    base = new[0][1]
    count = 1

    for i in range(len(new)) :
        if base > new[i][1] :
            count += 1
            base = new[i][1]

    print(count)