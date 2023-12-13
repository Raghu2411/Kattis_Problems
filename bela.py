do =    {
  "A": 11,
  "K": 4,
  "Q": 3,
  "J": 20,
  "T": 10,
  "9": 14,
  "8": 0,
  "7": 0
}
ndo =    {
  "A": 11,
  "K": 4,
  "Q": 3,
  "J": 2,
  "T": 10,
  "9": 0,
  "8": 0,
  "7": 0
}
inp = input("")
a = inp.split(" ")
count = 4*int(a[0])
dominant = a[1]
ans = 0
for i in range(count):
    aa = input("")
    card = aa[0]
    suit = aa[1]
    if suit == dominant:
        ans += int(do[card])
    else:
        ans += int(ndo[card])
print(ans)