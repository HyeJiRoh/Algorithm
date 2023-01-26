import sys
input = sys.stdin.readline

s = input().strip()
arr = []

for i in range(len(s)) :
    arr.append(s[i:])

arr.sort()

for i in arr :
    print(i)