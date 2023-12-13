inNums = []
inChar = []
out = []
s = ""
numbers = input().split(" ")
for i in numbers:
    inNums.append(i)
for j in inNums:
    out.append(int(j))
out.sort()
ch = input()
for k in ch:
    inChar.append(k)
A = out[0]
B = out[1]
C = out[2]
for g in range(2):
    if inChar[g] == 'A':
        s += str(A)+" "
        out.remove(int(A))
    elif inChar[g] == 'B':
        s+= str(B)+" "
        out.remove(int(B))
    else:
        s+= str(C)+" "
        out.remove(int(C))
print(s+str(out[0]))