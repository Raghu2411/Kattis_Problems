import math
inp = input("")
ans = []
while inp != "0 0 0 0 0":
    some = inp.split(" ")
    a = float(some[0])
    b = float(some[1])
    s = float(some[2])
    m = float(some[3])
    n = float(some[4])
    horizontal = a*m
    vertical = b*n
    angle = format(math.degrees(math.atan(vertical/horizontal)), '.2f')
    velocity = format(math.sqrt((vertical*vertical)+(horizontal*horizontal))/s, '.2f')
    ans.append(angle+" "+velocity)
    inp = input("")
for i in ans:
    print(i)