import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))