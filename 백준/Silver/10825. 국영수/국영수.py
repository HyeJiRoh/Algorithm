import sys
input = sys.stdin.readline

n = int(input())
student_list = []

for i in range(n) :
    name, kor, eng, math = list(input().strip().split())
    student_list.append((name, int(kor), int(eng), int(math)))

student_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in student_list :
    print(i[0])