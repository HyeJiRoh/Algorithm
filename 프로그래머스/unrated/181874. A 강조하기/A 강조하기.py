def solution(myString):
    answer = ''
    for word in myString:
        if word == "a" or word == "A":
            answer += "A"
        else:
            answer += word.lower()
    return answer