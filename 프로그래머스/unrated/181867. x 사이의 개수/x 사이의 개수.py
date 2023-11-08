def solution(myString):
    tmp = myString.split("x")
    answer = []
    for word in tmp:
        answer.append(len(word))
    return answer