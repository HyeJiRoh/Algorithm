def solution(people, limit):
    answer = 0

    people.sort()
    
    x, y = 0, len(people)-1
    
    while x < y:
        if people[x] + people[y] <= limit:
            x += 1
            answer += 1
        y -= 1
                
    return len(people) - answer