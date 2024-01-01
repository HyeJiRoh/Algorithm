def solution(number, k):
    stack = []
    for num in number:
        while len(stack) != 0 and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k != 0:
        return number[:-k]
    else:
        return ''.join(stack)