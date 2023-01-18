import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    str = input().strip()
    print(str[0]+str[-1])