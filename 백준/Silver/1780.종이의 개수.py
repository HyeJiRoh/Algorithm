import sys
input = sys.stdin.readline
 
n = int(input())
arr = []
p,m,z = 0,0,0
for i in range(n):
    arr.append(list(map(int,input().split())))
 
def solution(x,y,N) :
    global p,m,z
    color = arr[y][x]
    for i in range(y,y+N) :
        for j in range(x,x+N) :
            d = N//3
            if color != arr[i][j] :
                solution(x,y,d)
                solution(x+d,y,d)
                solution(x+(2*d),y,d)
                
                solution(x,y+d,d)
                solution(x+d,y+d,d)
                solution(x+(2*d),y+d,d)
                
                solution(x,y+(2*d),d)
                solution(x+d,y+(2*d),d)
                solution(x+(2*d),y+(2*d),d)
                return 
 
    if color == 1:
        p += 1
    if color == 0 :
        z += 1
    if color == -1 :
        m += 1
 
solution(0,0,n)
print(m,z,p,sep='\n')
