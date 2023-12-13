import sys
ask = input()
dic = {}
while ask != "":
    some = ask.split(" ")
    dic[some[1]] = some[0]
    ask = input()

for line in sys.stdin:
    line=line[:-1]
    if line in dic:
        print(dic[line])
    else:
        print("eh")