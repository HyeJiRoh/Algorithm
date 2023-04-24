def solution(s):
    arr = list(map(str, s))
    stack = []
    
    for word in arr:
        if word == '(':
            stack.append(word)
        elif word == ')':
            if '(' not in stack:
                stack.append(word)
                break
            else:
                stack.pop()
    
    if len(stack) != 0:
        return False
    else:
        return True