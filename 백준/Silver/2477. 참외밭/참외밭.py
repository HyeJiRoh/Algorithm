import sys
input = sys.stdin.readline

n = int(input())
arr = []
maxx = [(0,0),(0,0)]

for i in range(6):
    d,w = map(int,input().split())
    d = 0 if d<=2 else 1
    if w > maxx[d][1]:
        maxx[d] = (i,w)
    arr.append((d,w))
    
ans = maxx[0][1]*maxx[1][1]
check = [False]*6
for idx,_ in maxx:
    for i in idx,(idx+1)%6,idx-1:
        check[i] = True

min_square = 1
for i in range(6):
    if not check[i]:
        min_square *= arr[i][1]
print((ans-min_square)*n)