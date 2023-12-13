string = input("")
w = 0
l = 0
u = 0
s = 0
for i in string:
    if i.islower() == True:
        l +=1
    elif i.isupper() == True:
        u +=1
    elif i == "_":
        w +=1
    else:
        s +=1
length = len(string)
print(w / length)
print(l / length)
print(u / length)
print(s / length)