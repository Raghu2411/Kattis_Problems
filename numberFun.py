inp = int(input(""))
ans = []
for i in range(inp):
    num = input("").split(" ")
    f = int(num[0])
    s = int(num[1])
    t = int(num[2])
    if f+s == t:
        ans.append("Possible")
    elif abs(f-s) == t:
        ans.append("Possible")
    elif s*f == t:
        ans.append("Possible")
    elif f/s == t or s/f == t:
        ans.append("Possible")
    else:
        ans.append("Impossible")
for j in ans:
    print(j)