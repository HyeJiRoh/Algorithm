import sys
input = sys.stdin.readline

n = int(input())
birthday_list = []

for i in range(n) :
    name, dd, mm, yyyy = map(str, input().strip().split())
    birthday_list.append([name, int(dd), int(mm), int(yyyy)])

birthday_list.sort(key = lambda x: (x[3], x[2], x[1]))

print(birthday_list[-1][0])
print(birthday_list[0][0])