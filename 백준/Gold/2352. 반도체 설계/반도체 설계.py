from bisect import bisect_left

n = input()
arr = list(map(int, input().split()))
link = []
for check in arr:
    if not link or link[-1] < check:
        link.append(check)
    else:
        link[bisect_left(link, check)] = check
print(len(link))