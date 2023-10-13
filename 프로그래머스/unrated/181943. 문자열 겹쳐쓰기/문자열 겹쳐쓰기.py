def solution(my_string, overwrite_string, s):
    answer = ''
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s+len(overwrite_string):]
    return answer