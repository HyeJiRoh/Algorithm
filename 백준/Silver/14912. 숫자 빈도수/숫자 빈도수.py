import sys
input = sys.stdin.readline

n, d = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]

result = 0

for number in arr:
    if str(d) in number:
        result += number.count(str(d))

print(result)