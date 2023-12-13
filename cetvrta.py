x = []
y = []
x4 = 0
y4 = 0
for i in range(3):
    points = input("").split(" ")
    x.append(points[0])
    y.append(points[1])
x1,x2,x3 = int(x[0]),int(x[1]),int(x[2])
y1,y2,y3 = int(y[0]),int(y[1]),int(y[2])
if x1 == x2:
    x4 = x3
elif x2 == x3:
    x4 = x1
else:
    x4 = x2

if y1 == y2:
    y4 = y3
elif y2 == y3:
    y4 = y1
else:
    y4 = y2

print(str(x4)+" "+str(y4))