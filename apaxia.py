ans = []
nice = ""
i = 0
ask = input("") + "!"
for k in ask:
    while i < (len(ask)-1):
        if ask[i] == ask[i+1]:
            pass
        else:
            ans.append(ask[i])
        i+=1
for j in ans:
    nice += j
print(nice)