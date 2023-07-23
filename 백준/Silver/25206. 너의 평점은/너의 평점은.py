import sys
input = sys.stdin.readline

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	
result = 0
	
for _ in range(20) :
    subject, total_score, final_grade = input().split()
    total_score = float(total_score)
    if final_grade != 'P' :	
        total += total_score
        result += total_score * grade[rating.index(final_grade)]

print('%.6f' % (result / total))