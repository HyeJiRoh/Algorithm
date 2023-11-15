def solution(my_string, s, e):
    answer = ''
    head = my_string[:s]
    reverse = my_string[s:e+1][::-1]
    tail = my_string[e+1:]
    answer = head + reverse + tail
    return answer