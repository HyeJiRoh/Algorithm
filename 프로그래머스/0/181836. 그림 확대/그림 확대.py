def solution(picture, k):
    answer = []
    
    for pic in picture: 
        tmp = ''
        
        for pixel in pic:
            tmp += pixel * k
        
        for _ in range(k):
            answer.append(tmp) 
    
    return answer