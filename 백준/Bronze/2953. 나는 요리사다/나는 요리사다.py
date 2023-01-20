import sys
input = sys.stdin.readline

score = []

for i in range(5) :
    arr = list(map(int, input().split()))
    score.append(sum(arr))

print(score.index(max(score))+1, max(score))