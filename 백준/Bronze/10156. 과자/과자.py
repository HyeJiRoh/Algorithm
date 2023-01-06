k, n, m = map(int, input().split())
total = k*n
gap = total-m

if gap>0 :
    print(gap)
else :
    print(0)