num = int(input())
answer = 1
count = 0 

for i in range(1, num+1) :
  answer *= i

answer = str(answer)
answer = answer[::-1]

for i in answer :
  if i != '0' :
    break
  else :
    count += 1

print(count)