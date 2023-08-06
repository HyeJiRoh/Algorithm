from itertools import combinations_with_replacement

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()  

num = list(set(combinations_with_replacement(num, m)))

for result in num:
    print(*result)