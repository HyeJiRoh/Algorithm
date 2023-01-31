import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n) :
    i = int(input())
    arr.append(i)

arr.sort(reverse=True)

for i in arr :
    print(i)