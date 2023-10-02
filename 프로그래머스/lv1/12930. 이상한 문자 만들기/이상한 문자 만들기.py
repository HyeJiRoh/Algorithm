def solution(s):
    answer = ''
    words = list(s.split(' '))
    
    for word in words:
        for idx in range(len(word)):
            if idx % 2 == 0:
                answer += word[idx].upper()
            else:
                answer += word[idx].lower()
        answer += " "
    
    return answer[:-1]