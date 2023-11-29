def solution(brown, yellow):
    area = brown + yellow
    for y in range(1, area + 1):
        if (area / y) % 1 == 0:
            x = area / y
            if x >= y and 2*x + 2*y == brown + 4:
                return [x, y]  