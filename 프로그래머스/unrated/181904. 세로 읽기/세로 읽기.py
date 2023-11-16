def solution(my_string, m, c):
    answer = ''
    my_string = list(my_string)
    for i in range(0, len(my_string), m):
        answer += my_string[i+c-1]
    return answer