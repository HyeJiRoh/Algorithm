def solution(array, commands):
    answer = []
    for num in commands:
        i, j, k = num[0], num[1], num[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer