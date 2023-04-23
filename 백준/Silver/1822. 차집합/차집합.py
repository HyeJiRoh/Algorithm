import sys
input = sys.stdin.readline

a, b = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = []

for a_num in A:
    if a_num not in B:
        result.append(a_num)

result.sort()
print(len(result))

if len(result) > 0:
    print(*result)
