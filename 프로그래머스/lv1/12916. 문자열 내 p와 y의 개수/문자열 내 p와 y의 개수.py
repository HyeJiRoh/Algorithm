def solution(s):
    answer = 0
    s = s.lower()
    if s.count('p') == s.count('y') :
        answer = bool(1)
    elif s.count('p') != s.count('y') :
        answer = bool(0)
    return answer