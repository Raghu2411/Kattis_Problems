import sys
for line in sys.stdin:
    inpp = line.split(" ")
    f = int(inpp[0])
    s = int(inpp[1])
    print(abs(f-s))