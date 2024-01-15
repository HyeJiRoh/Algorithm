import sys
sys.setrecursionlimit(10**6)
 
n,row,col = map(int,input().split())
 
def z(h,w,N):
    if row == h and col == w:
        return 0
 
    b = 2**(N-1)  # 좌표 옮길 때 idx 값 변화, 사각형 절반 길이
 
    if row < h+b:
        if col < w+b:  # 2사분면
            return z(h,w,N-1)
        else:  # 1사분면
            return b*b+z(h,w+b,N-1)
    else:
        if col < w+b:  # 3사분면
            return 2*b*b+z(h+b,w,N-1)
        else:  # 4사분면
            return 3*b*b+z(h+b,w+b,N-1)
 
print(z(0,0,n))
