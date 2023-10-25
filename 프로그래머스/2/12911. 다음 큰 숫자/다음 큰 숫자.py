def solution(n):
    answer = 0
    data = str(bin(n))
    for num in range(n+1, 1000001):
        num_data = str(bin(num))
        if num_data.count('1') == data.count("1"):
            return num