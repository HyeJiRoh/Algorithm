import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    candy, sons = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)."%(candy//sons, candy % sons))