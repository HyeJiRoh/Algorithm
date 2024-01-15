N, M = map(int, input().split())
img1, img2 = [input() for _ in range(N)], [input() for _ in range(N)]
eyfa = True 

for i in range(N) :
    # img1과 비교
    compare = ''
    # img*2와 비교
    compare += j*2
    if compare!= img2[i]:
    	eyfa = False
        break
print('Eyfa' if eyfa else 'Not Eyfa')
