import sys
input = sys.stdin.read

s = input().replace("\n", "").replace(" ", "")
word = [0] * 26

for i in s:
    word[ord(i) - 97]+=1
    
max_value = max(word)
result = []

for i in range(len(word)):
    if word[i] == max_value:
        result.append(chr(i+97))
        
result.sort()
print(*result, sep="")