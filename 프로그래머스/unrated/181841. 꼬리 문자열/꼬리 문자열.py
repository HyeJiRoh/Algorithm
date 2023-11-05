def solution(str_list, ex):
    answer = ''
    for word in str_list:
        if ex not in word:
            answer += word
    return answer