import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    print(2 - a + b)