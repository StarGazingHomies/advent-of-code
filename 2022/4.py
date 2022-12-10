def isFullyContained(a, b, c, d):
    return (a<=c and b>=d) or (a>=c and b<=d)

def overlapAtAll(a, b, c, d):
    return (a <= d) and (c <= b)


if __name__ == '__main__':
    with open('4.in','r') as fin:
        lns = fin.readlines()
    cnt1 = 0
    cnt2 = 0
    for ln in lns:
        a, b = ln.split(',')[0].split('-')
        c, d = ln.split(',')[1].split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)
        if (isFullyContained(a, b, c, d)):
            cnt1 += 1
        if (overlapAtAll(a, b, c, d)):
            cnt2 += 1
    print(cnt1, cnt2)
