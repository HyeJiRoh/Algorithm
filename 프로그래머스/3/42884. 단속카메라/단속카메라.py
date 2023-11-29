def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 1
    passed = routes[0][1]
    
    for start, end in routes :
        if start > passed :
            answer += 1
            passed = end

    return answer
