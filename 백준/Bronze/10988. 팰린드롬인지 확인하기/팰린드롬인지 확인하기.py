import sys

input = sys.stdin.readline
str = input().rstrip()

if str[::-1] == str :
    print(1)
else :
    print(0)