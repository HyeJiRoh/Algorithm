import sys

input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N) :
    a, b, c = map(int, input().split())

    if a==b==c :
        result = max(result, 10000+a*1000)
    elif a==b :
        result = max(result, 1000+a*100)
    elif b==c :
        result = max(result, 1000+b*100)
    elif c==a :
        result = max(result, 1000+c*100)
    else :
        result = max(result, 100*max(a,b,c))

print(result)