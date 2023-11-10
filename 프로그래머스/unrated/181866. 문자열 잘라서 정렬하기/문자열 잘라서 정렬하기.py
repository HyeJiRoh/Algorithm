def solution(myString):
    answer = list(filter(None, myString.split('x')))
    answer.sort()
    return answer