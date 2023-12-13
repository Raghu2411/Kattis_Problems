import math
score = 0
tc = int(input(""))
ans = []
for j in range(tc):
    throw = int(input(""))
    for k in range(throw):
        xy = input("").split(" ")
        x = int(xy[0])
        y = int(xy[1])
        dist = math.sqrt((x**2) + (y**2))
        if dist == 0:
            score -=1
        
        while dist<=200:
            score+=1
            dist+=20
    ans.append(score)
    score = 0
for i in ans:
    print(i)