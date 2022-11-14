import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(1, n+1) :
  pokemon = input().strip()
  dict[i] = pokemon
  dict[pokemon] = i

for i in range(m) :
  q = input().strip()
  if q.isdigit() :
    print(dict[int(q)])
  else :
    print(dict[q])