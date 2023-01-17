import sys
input = sys.stdin.readline

A = int(input())
operation = input().strip()
B = int(input())

if operation == '+':
    print(A+B)
else :
    print(A*B)