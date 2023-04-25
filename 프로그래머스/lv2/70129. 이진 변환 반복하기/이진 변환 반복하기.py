def solution(s):
    s = str(s)
    zero_cnt = 0
    cnt = 0
    
    while True:
        if s == '1':
            break
            
        zero_cnt += s.count('0')
        
        s = s.replace('0', '')
            
        tmp = bin(len(s))[2:]
        s = tmp
        cnt += 1

    answer = [cnt, zero_cnt]
    return answer