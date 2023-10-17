def solution(my_string, alp):
    answer = ''
    for word in my_string:
        if word == alp:
            answer += word.upper()
        else:
            answer += word
    return answer