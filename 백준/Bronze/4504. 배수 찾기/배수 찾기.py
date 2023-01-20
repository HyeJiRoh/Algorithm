import sys
input = sys.stdin.readline

n = int(input())

while True :
    k = int(input())

    if k==0 :
        break

    if k%n != 0 :
        print("%d is NOT a multiple of %d."%(k, n))
    else :
        print("%d is a multiple of %d."%(k, n))