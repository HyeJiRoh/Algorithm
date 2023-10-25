def solution(s):
    stack = []
    for word in s:
        if len(stack) == 0 or stack[-1] != word:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
    if len(stack):
        return 0
    else:
        return 1