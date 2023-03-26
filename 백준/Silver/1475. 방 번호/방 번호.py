import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
arr = [0 for _ in range(10)]

idx = 0
special_cnt = 0

for idx in n:
    if idx == 6 or idx == 9:
        special_cnt += 1 
    else:
        arr[idx] += 1 

if special_cnt % 2 == 0 :
    max_cnt = special_cnt // 2
else:
    max_cnt = special_cnt // 2 + 1

print(max(max(arr), max_cnt))