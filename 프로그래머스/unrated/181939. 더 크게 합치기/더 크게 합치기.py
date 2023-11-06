def solution(a, b):
    answer = 0
    
    tmp_a = str(a) + str(b)
    tmp_b = str(b) + str(a)
    
    if int(tmp_a) >= int(tmp_b):
        answer = tmp_a
    elif int(tmp_b) > int(tmp_a):
        answer = tmp_b
    return int(answer)