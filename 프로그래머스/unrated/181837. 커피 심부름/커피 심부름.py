def solution(order):
    answer = 0
    for coffee in order:
        if coffee == "icecafelatte" or coffee == "cafelatteice" or coffee == "hotcafelatte" or coffee == "cafelattehot" or coffee == "cafelatte":
                answer += 5000
        else:
            answer += 4500
              
    return answer