ans = []
inp = input("")
checker = "PER"*int(len(inp)/3)
# print(inp)
# print(checker)
for i in range(len(inp)):
    if inp[i] != checker[i]:
        ans.append(inp[i])
    else:
        pass
print(len(ans))