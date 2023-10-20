def solution(rny_string):
    answer = ''
    for word in rny_string:
        if word == 'm':
            answer += 'rn'
        else:
            answer += word
    return answer