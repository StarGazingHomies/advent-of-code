if __name__ == '__main__':
    with open("10.in","r") as fin:
        lns = fin.readlines()

    prgmCnt = -1
    X = 1
    result = 0
    interest = [20,60,100,140,180,220]
    for ln in lns:
        if ln[:4] == "noop":
            prgmCnt += 1
##            print(prgmCnt, X, abs(prgmCnt % 40 - X), abs(prgmCnt % 40 - X)<=1)
            if abs(prgmCnt % 40 - X) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            if prgmCnt % 40 == 39:
                print()
        else:
            prgmCnt += 1
##            print(prgmCnt, X, abs(prgmCnt % 40 - X), abs(prgmCnt % 40 - X)<=1)
            if abs(prgmCnt % 40 - X) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            if prgmCnt % 40 == 39:
                print()
                
            prgmCnt += 1
##            print(prgmCnt, X, abs(prgmCnt % 40 - X), abs(prgmCnt % 40 - X)<=1)
            if abs(prgmCnt % 40 - X) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            if prgmCnt % 40 == 39:
                print()
  
            X += int(ln[5:])  
        
    print(prgmCnt, X)        
