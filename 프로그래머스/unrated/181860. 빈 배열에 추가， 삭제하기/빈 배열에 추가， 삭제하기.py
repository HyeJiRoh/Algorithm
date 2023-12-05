def solution(arr, flag):
    answer = []

    for idx in range(len(flag)):
        if flag[idx]:
            for _ in range(arr[idx]*2):
                answer.append(arr[idx])
        else:
            for _ in range(arr[idx]):
                answer.pop()
    return answer