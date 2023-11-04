def solution(arr, delete_list):
    answer = []
    for num in arr:
        if num not in delete_list:
            answer.append(num)
    return answer