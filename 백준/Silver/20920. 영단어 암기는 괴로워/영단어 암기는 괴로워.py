import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
word_list = {}

for _ in range(N):
    word = input().rstrip()
    
    if len(word) < M: 
        continue
    else: 
        if word in word_list:
            word_list[word] += 1
        else: 
            word_list[word] = 1

word_list = sorted(word_list.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_list:
    print(i[0])