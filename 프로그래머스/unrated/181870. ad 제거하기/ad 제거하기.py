def solution(strArr):
    answer = []
    for word in strArr:
        if "ad" not in word:
            answer.append(word)
    return answer