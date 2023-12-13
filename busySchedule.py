inp = int(input(""))
am = []
pm = []
ans = []
temp = []
temp2 = []
while inp != 0:
    for i in range(inp):
        a = input("")
        start = a[0]+a[1]
        last = a[-4]+a[-3]+a[-2]+a[-1]
        if start == "12" and last == "a.m.":
            temp.append(a)
        elif start == "12" and last == "p.m.":
            temp2.append(a)
        else:
            aa = a.split(" ")
            aaa = aa[0]
            b = float(aaa.replace(":","."))
            if aa[1] == "a.m." and aaa != "12:00":
                am.append(b)
            elif aa[1] == "p.m." and aaa != "12:00":
                pm.append(b)
            else:
                pass
    temp.sort()
    temp2.sort()
    am.sort()
    pm.sort()
    if len(temp) >= 1:
        for h in temp:
            ans.append(h)
    else:
        pass
    for j in am:
        bb = format(j, '.2f')
        some = bb.replace(".",":") + " a.m."
        ans.append(some)
    if len(temp2) >= 1:
        for hh in temp2:
            ans.append(hh)
    else:
        pass
    for k in pm:
        bb1 = format(k, '.2f')
        some1 = bb1.replace(".",":") + " p.m."
        ans.append(some1)
    am.clear()
    pm.clear()
    temp.clear()
    temp2.clear()
    inp = int(input(""))
    if inp != 0:
        ans.append("")
    else:
        pass
for n in ans:
    print(n)