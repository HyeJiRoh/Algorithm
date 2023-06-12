import sys
input = sys.stdin.readline

str = input().rstrip()
word_stack = []
tag = False
res = ''

for word in str:
    if word == " ":
        while word_stack:
            res += word_stack.pop()
        res += word

    elif word == "<":
        while word_stack:
            res += word_stack.pop()
        tag = True
        res += word

    elif word == ">":
        tag = False
        res += word

    elif tag:
        res += word

    else:
        word_stack.append(word)


while word_stack:
    res += word_stack.pop()
print(res)