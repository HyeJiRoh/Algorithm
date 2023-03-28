import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key = lambda x: (x[1], x[0]))

before_end = 0
cnt = 0

for meeting in meetings:
    start = meeting[0]
    end = meeting[1]

    if start >= before_end:
        cnt += 1
        before_end = end

print(cnt)