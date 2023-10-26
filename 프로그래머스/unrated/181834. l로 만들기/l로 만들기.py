def solution(myString):
    answer = ''

    for word in myString:
        if ord(word) < ord('l'):
            answer += 'l'
        else:
            answer += word
            
    return answer