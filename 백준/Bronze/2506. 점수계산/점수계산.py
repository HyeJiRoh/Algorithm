import sys
input = sys.stdin.readline

t = int(input())
arr = list(map(int, input().split()))
score = total = arr[0]

for i in range(1, len(arr)) :
    if arr[i] == 1 and arr[i-1] == 0:
        score = 1
    elif arr[i] == 1 and arr[i-1] == 1 :
        score += 1
    else :
        score = 0
    total += score

print(total)