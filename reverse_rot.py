ans = []
out = []
result = []
some2 = ""
inp = ""

while inp != "0":
    inp = input("")
    if inp != "0":
        ans.append(inp)
    else:
        pass

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
for i in ans:
    splitted = i.split(" ")
    n = int(splitted[0])
    syn = splitted[1].strip().upper()
    rever = syn[::-1]
    for j in rever:
        findA = alpha.index(j)
        some = alpha[findA+n]
        result.append(some)  #converted
    for c in result:
        some2 += c
    out.append(some2)
    result.clear()
    some2 = ""

for f in out:
    print(f)