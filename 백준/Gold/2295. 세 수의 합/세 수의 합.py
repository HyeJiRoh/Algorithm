import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

answer = 0

cache = {}

arr.sort()
for i in arr:
    for j in arr:
        cache.setdefault(i + j, True)

flag = False
for last in range(N-1, -1, -1):

    if(flag): break

    for num in range(last + 1):
        if(arr[last] - arr[num] in cache):
            answer = arr[last]
            flag = True
            break

print(answer)