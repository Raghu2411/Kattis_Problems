inp = int(input(""))
ans = []
for i in range(inp):
    a = int(input(""))
    if a%2 == 0:
        ans.append(str(a)+" is even")
    else:
        ans.append(str(a)+" is odd")
for j in ans:
    print(j)