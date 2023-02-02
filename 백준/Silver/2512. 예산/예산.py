import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())

start = 0
end = max(array)

while start<=end :
    total = 0
    result = 0
    mid = (start+end)//2

    for price in array:
        if price > mid :
            total+=mid
        else:
            total+=price

    if total <= M:
        start = mid+1
    else:
        end = mid-1

print(end)