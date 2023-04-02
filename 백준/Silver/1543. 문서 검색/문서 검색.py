import sys
input = sys.stdin.readline

docs = input().strip()
word = input().strip()

result = docs.split(word)

print(len(result)-1)