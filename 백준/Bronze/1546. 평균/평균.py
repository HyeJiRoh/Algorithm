num = int(input())
score = list(map(int, input().split()))
max_score = max(score)

for i in range(num):
    score[i] = score[i]/max_score*100
print("%.2f" %(sum(score)/ num))