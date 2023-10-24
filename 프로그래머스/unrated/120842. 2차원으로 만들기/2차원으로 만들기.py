def solution(num_list, n):
    answer = [[] for i in range(len(num_list) // n)]
    cnt, idx = 0, 0

    for num in num_list:
        cnt += 1
        answer[idx].append(num)
        
        if cnt == n:
            cnt = 0
            idx += 1
            
    return answer