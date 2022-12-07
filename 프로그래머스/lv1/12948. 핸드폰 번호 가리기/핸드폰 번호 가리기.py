def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4) :
        answer += '*'
    answer += phone_number[-4]
    answer += phone_number[-3]
    answer += phone_number[-2]
    answer += phone_number[-1]
        
    return answer