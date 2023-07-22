import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
li = list(map(int, input().split()))
X = int(input())

result = []

for i in range(N):
    if li[i] != X:
        if gcd(li[i], X) == 1:
            result.append(li[i])

print("{:.6f}".format(sum(result) / len(result)))