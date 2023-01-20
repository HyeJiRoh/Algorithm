import sys
input = sys.stdin.readline

ban = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr :
    if i%10 == ban :
        count += 1

print(count)