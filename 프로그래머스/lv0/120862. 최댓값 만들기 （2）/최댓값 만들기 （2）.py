def solution(numbers):
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    if numbers[0]*numbers[1]>=0 and numbers[0]*numbers[1]>=answer:
        answer = numbers[0]*numbers[1]
    return answer