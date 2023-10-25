def solution(n):
    answer = 0
    for num in range(n+1, 1000001):
        if str(bin(num)).count('1') == str(bin(n)).count("1"):
            return num