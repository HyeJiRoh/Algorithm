import sys
input = sys.stdin.readline

n = int(input())
name_list = dict()

for i in input().split():
  name_list[i] = 0

for _ in range(n):
  for i in input().split():
    name_list[i] += 1

for i in sorted(name_list.items(), key=lambda x:(-x[1], x[0])):
  print(*i)