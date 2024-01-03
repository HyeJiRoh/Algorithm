import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
T = list(t)

while True:
    if len(s) == len(T):
        break    
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T=T[::-1]

result = "".join(T)
if s == result:
    print(1)
else: print(0)