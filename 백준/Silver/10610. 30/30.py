import sys
input = sys.stdin.readline

n = list(input().strip())
n.sort(reverse=True)
total = 0

for i in n :
    total += int(i)

if '0' not in n or total%3 != 0 :
    print(-1)
else :
    print(''.join(n))