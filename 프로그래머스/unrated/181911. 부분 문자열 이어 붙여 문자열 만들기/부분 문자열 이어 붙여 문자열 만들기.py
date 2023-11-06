def solution(my_strings, parts):
    answer = ''
    for idx in range(len(my_strings)):
        start, end = parts[idx]
        answer += my_strings[idx][start:end+1]
    return answer