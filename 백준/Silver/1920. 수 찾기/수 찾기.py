import sys
input = sys.stdin.readline

n = int(input())
nrr = list(map(int, input().split()))

m = int(input())
mrr = list(map(int, input().split()))

nrr.sort()

for num in mrr:
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2

        if num == nrr[mid]:
            print(1)
            break

        elif num > nrr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    if start > end:
        print(0)