def solution(my_string):
    answer = ''
    my_string = sorted(my_string.lower())
    for i in my_string :
        answer += i
    return answer