import sys
input = sys.stdin.readline

n = int(input())

for i in range(n) :
    str = input().strip()
    str = str[0].upper() + str[1:]
    print(str)