answer_log = []
pos = []
count = int(input(""))
for i in range(count):
    ask = input("")
    aa =ask.split(" ")
    dataset = aa[0]
    aaa = aa[1].split("/")
    nume = int(aaa[0])
    deno = int(aaa[1])
    while nume>1 or deno>1:
        if nume>deno:
            nume = nume - deno
            pos.append("R")
        else:
            deno = deno - nume
            pos.append("L")
    rever = pos[::-1]
    value = 1
    for j in rever:
        value = value * 2
        if j == "R":
            value = value + 1
    pos.clear()
    rever.clear()
    answer = "{} {}"
    answer_log.append(answer.format(dataset,value))

for k in answer_log:
    print(k)