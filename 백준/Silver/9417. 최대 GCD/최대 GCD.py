import sys
input = sys.stdin.readline

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(n):
    numbers = sorted(list(map(int, input().split())))
    result = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(gcd(max(numbers[i], numbers[j]), min(numbers[i], numbers[j])))

    print(max(result))
