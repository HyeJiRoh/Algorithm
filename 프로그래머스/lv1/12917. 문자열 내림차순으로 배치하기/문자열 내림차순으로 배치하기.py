def solution(s):
    answer = ''
    answer = list(str(s))
    answer.sort(reverse = True)
    answer = "".join(answer)
    return answer