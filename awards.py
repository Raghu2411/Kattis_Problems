ans = []
uni = []
winner = []
l = 0
count = int(input(""))
for x in range(count):
    a = input("")
    ans.append(a)
    while l<12:
        aa = a.split(" ")
        if aa[0] in uni:
            break
        else:
            uni.append(aa[0])
            winner.append(a)
            l = l+1
            break

for j in winner:
    print(j)