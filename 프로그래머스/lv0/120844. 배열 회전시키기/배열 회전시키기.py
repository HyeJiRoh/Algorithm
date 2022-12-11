def solution(numbers, direction):
    answer = []
    if direction == "right" :
        answer.append(numbers[-1])
        for i in numbers :
            answer.append(i)
        answer = answer[:len(numbers)]
    elif direction == "left" :
        for i in range(1, len(numbers)) :
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer