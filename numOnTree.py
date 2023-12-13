def root(level):
    return (1 << (level + 1)) - 1

def travel_down(n,direct,t_root):
    n = t_root-(((t_root-n)*2) + (1 if direct=='R' else 0))
    return n



inp=input().split()
if len(inp)==1:
    h=int(inp[0])
    strr=''
else:
    h,strr=inp
    h=int(h)

n=root(h)
t_root=n+1
for i in range(len(strr)):
    n=travel_down(n,strr[i], t_root)

print(n)