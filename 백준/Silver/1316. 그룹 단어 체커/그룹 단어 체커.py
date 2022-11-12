num = int(input())
count = 0

for i in range(num) :
  text = list(input())
  a = [] # 입력받은 문자의 인덱스
  b = [] # a의 오름차순 값
  
  for k in text :
    a.append(text.index(k))
    b.append(text.index(k))
    b.sort()
    
  if a == b :
    count += 1
      
print(count)