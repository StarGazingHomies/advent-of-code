def getResult(a,b):
    m = ord(a)-ord('A')
    n = ord(b)-ord('X')
    if (m-n)%3==1:
        r = 0
    elif (m-n)%3==2:
        r = 6
    else:
        r = 3

    return r+n+1

def getResult_Part2(a, b):
    m = ord(a)-ord('A')
    n = ord(b)-ord('X')-1
    # -1 lose, 0 draw, 1 win
    choice = (m+n)%3

    return choice+4+n*3
    

if __name__ == '__main__':
    with open("2.in","r") as fin:
        lns = fin.readlines()

    score = 0
    for ln in lns:
        a, b = ln.split(' ')
        a = a[0]
        b = b[0]
        score += getResult_Part2(a,b)
