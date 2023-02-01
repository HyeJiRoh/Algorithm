import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    index, str = input().strip().split()
    index = int(index)-1
    str = list(str)
    str[index] = ''
    print(''.join(str))