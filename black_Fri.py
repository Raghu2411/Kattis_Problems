data = []
new_data = []
rem = []
count = 0
inp = int(input(""))
a = input("")
aa = a.split(" ")
for i in range(inp):
    data.append(int(aa[i]))
my_set = set(data)
new_data = list(my_set)
for k in new_data:
    count = data.count(k)
    if count > 1:
        rem.append(k)
    else:
        pass
for n in rem:
    new_data.remove(n)
new_data.sort()
length = len(new_data)
if length == 0:
    print("none")
else:
    maxi = new_data[length-1]
    answer = data.index(maxi)
    print(answer + 1)