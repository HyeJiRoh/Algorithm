def solution(strArr):
    answer = []
    for idx in range(len(strArr)):
        if idx % 2 != 0:
            answer.append(strArr[idx].upper())
        else:
            answer.append(strArr[idx].lower())
    return answer