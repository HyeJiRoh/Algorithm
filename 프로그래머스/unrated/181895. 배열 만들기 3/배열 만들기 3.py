def solution(arr, intervals):
    answer = []
    for data in intervals:
        for i in range(data[0], data[-1]+1):
            answer.append(arr[i])
    return answer