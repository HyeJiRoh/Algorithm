import sys
input = sys.stdin.readline

n = int(input())

score = []

for _ in range(n):
    score.append(float(input()))

score.sort()

for i in range(7):
    print("{:.3f}".format(score[i]))