d = int(input())
for i in range(d):
    n, sl_h, sl_m = map(int, input().split())
    start = (sl_h*60) + sl_m
    day = 1440
    for j in range(n):
        h, m = map(int, input().split())
        alarm = (h * 60) + m
        temp = 03
        if alarm < start:
            temp = (1440 - start) + alarm
        else:
            temp = alarm - start
        day = min(day, temp)
    print(day // 60, day % 60)
