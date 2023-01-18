import sys
input = sys.stdin.readline

T = int(input())
vote = list(input().strip())
a = vote.count('A')
b = vote.count('B')

if a>b :
    print('A')
elif a<b :
    print('B')
else :
    print("Tie")