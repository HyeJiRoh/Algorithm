import sys
input=sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
#서로소: lcm(a,b)==a*b or gcd(a,b)==1

n=int(input().rstrip()) #수의 개수
a=list(map(int,input().split()))  #수열
x=int(input().rstrip())  #x

mean=[]
for i in range(n):
    if a[i]!=x: #x와 같은 수가 아니면서
        if gcd(a[i],x)==1: #gcd(a,b)==1인 것
            mean.append(a[i])

print('{:.6f}'.format(sum(mean)/len(mean)))