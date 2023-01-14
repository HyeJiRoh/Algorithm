import sys

resistance = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6', 'violet':'7', 'grey':'8', 'white':'9'}
mix_color = ''

for i in range(2) :
    color = sys.stdin.readline().rstrip()
    mix_color += resistance[color]

last_color = sys.stdin.readline().rstrip()
multi = 10**int(resistance[last_color])

mix_color = int(mix_color)

print(mix_color*multi)