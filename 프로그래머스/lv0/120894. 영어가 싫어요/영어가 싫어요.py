def solution(numbers):
    answer = []
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in alpha :
        if i in numbers :
            numbers = numbers.replace(i, str(alpha.index(i)))
    answer = int(numbers)
    return answer