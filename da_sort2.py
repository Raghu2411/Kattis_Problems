def sorter(arr):
    lo,min_to_move, mtm_i,to_move = (1000000001,1000000001,len(arr),set())
    for i,c in enumerate(reversed(arr)):
        if c > lo:
            to_move.add(len(arr)-1-i)
            if c <= min_to_move:
                min_to_move = c
                mtm_i = len(arr)-1-i
        else:
            lo = c
    if arr[-1] == min_to_move:
        return len(to_move)

    for i,c in enumerate(arr[mtm_i+1:]):
        if c > min_to_move:
            to_move.add(mtm_i+1+i)

    return len(to_move)

def main():
    for i in range(int(input())):
        _,c = map(int,input().split())
        lis = []
        for _ in range(c // 10 + (1 if c % 10 > 0 else 0)):
            lis.extend(map(int,input().split()))
        ops = sorter(lis)
        print(f'{i+1} {ops}')

if __name__ == "__main__":
    main()