def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer