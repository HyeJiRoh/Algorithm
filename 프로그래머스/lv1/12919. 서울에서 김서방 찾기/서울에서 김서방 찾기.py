def solution(seoul):
    answer = ''
    for i in seoul :
        if i == 'Kim' :
            answer = "김서방은 " + str(seoul.index(i)) + "에 있다"
    return answer