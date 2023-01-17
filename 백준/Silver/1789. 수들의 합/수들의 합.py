import sys
input = sys.stdin.readline

N = int(input())
count = 0
base = 1

while True  :
    N -= base
    if N < 0 :
        break
    base += 1
    count +=1

print(count)