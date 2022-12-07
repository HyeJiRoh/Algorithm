def solution(s):
    answer = []
    s = list(s)
    for i in s :
        if s.count(i) == 1 :
            answer += i
    answer.sort()
    answer = "".join(answer)
    return answer