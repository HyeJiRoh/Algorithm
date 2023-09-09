import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def count_2(N):
    if N < 2:
        return 0
    
    count = 0
    while N >= 2:
        count += N//2
        N = N//2
    return count

def count_5(N):
    if N < 5:
        return 0
    
    count = 0
    while N >= 5:
        count += N//5
        N //= 5
    return count

two_cnt = count_2(n) - count_2(n-m) - count_2(m)
five_cnt = count_5(n) - count_5(n-m) - count_5(m)
print(min(two_cnt, five_cnt))