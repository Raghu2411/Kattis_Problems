ans = []
inp = input("")
d = inp.split(" ")
d1 = int(d[0])
d2 = int(d[1])
if d1 == d2:
    print(d1+1)
elif d1 > d2:
    count = d1 - d2
    for i in range(count+1):
        d2 += 1
        ans.append(d2)
else:
    count = d2 - d1
    for j in range(count+1):
        d1 += 1
        ans.append(d1)
for k in ans:
    print(k)