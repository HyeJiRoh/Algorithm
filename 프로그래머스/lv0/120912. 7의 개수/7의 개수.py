def solution(array):
    answer = ''
    for i in array :
        answer += str(i)
    answer = answer.count("7")
    return answer