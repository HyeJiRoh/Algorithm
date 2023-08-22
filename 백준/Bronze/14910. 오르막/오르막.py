import sys

input = sys.stdin.readline

data = list(map(int, input().split()))
base = data[0]
flag = 0

if len(data) == 1:
    flag = 0
else:
    for i in range(1, len(data)):
        if data[i] >= base:
            base = data[i]
            continue
        else:
            flag = 1
            break

if flag == 0:
    print("Good")
else:
    print("Bad")
