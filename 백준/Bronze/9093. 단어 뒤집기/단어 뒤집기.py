import sys
input = sys.stdin.readline

T = int(input())
for str in range(T) :
    str = list(input().strip().split())
    for k in str :
        print(k[::-1], end = " ")