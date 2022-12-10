def cycle(increment = 0):
    global prgmCnt, result, interest, X
    if abs(prgmCnt % 40 - X) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if prgmCnt % 40 == 39:
        print()
    prgmCnt += 1
    if prgmCnt in interest:
        result += X * prgmCnt
    X += increment

if __name__ == '__main__':
    with open("10.in","r") as fin:
        lns = fin.readlines()

    prgmCnt = 0
    X = 1
    result = 0
    interest = [20,60,100,140,180,220]
    for ln in lns:
        if ln[:4] == "noop":
            cycle()
        else:
            cycle()
            cycle(int(ln[5:]))
        
    print("Part 1:", result)
