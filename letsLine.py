ans = []
r_li = []
count = int(input())
for j in range(count):
    a = input()
    ans.append(a)
s_li = sorted(ans)
for i in s_li:
    r_li.append(i)
r_li.reverse()
if ans == s_li:
    print("INCREASING")
elif ans == r_li:
    print("DECREASING")
else:
    print("NEITHER")