h, m = map(int, input().split())
total = h*60+m-45

hour = total//60
if(hour<0 or hour>24) :
  hour %= 24

minute = total%60

print(hour, minute)