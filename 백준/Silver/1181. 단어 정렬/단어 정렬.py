import sys
input = sys.stdin.readline

n = int(input())
word = []

for _ in range(n):
    word.append(input().strip())

word = list(set(word))
word.sort(key=lambda x:(len(x), x))

for i in word:
    print(i)