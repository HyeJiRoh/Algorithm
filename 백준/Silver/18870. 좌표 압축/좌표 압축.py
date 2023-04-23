import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = sorted(set(arr))

num_dict = {temp[i] : i for i in range(len(temp))}

for i in arr:
    print(num_dict[i], end = ' ')