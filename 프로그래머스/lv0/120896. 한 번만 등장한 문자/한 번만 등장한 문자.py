def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    for alpha in s:
        if s.count(alpha) == 1:
            answer += alpha
    return answer