import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    num = int(input())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

result = sorted(dict.items(), key = lambda x:(-x[1], x[0]))
print(result[0][0])