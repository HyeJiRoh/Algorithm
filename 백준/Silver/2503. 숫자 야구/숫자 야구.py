import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

data = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
num = list(permutations(data, 3))

for _ in range(N):
    number, strike, ball = map(int, input().split())
    number = list(str(number))
    cnt = 0
    for i in range(len(num)):
        strike_cnt = ball_cnt = 0
        i -= cnt
        for j in range(3):
            if num[i][j] == number[j]:
                strike_cnt += 1
            elif number[j] in num[i]:
                ball_cnt += 1

        if (strike_cnt != strike) or (ball_cnt != ball):
            num.remove(num[i])
            cnt += 1

print(len(num))
