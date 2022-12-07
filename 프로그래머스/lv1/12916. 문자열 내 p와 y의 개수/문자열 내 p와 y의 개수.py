def solution(s):
    answer = 0
    s = s.lower()
    if s.count('p') == s.count('y') :
        answer = True
    elif s.count('p') != s.count('y') :
        answer = False
    return answer