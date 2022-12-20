import functools
import sys
import math
import time

def ints(line):
    i = 0
    rtrns = []
    while i < len(line):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0', '-']:
            j = i + 1
            while j < len(line) and line[j] in ['1','2','3','4','5','6','7','8','9','0', '-']:
                j += 1
            
            rtrns.append(int(line[i:j]))
            i = j
        i += 1
    return rtrns


if __name__ == '__main__':
    with open('20.in','r') as fin:
        lns = fin.readlines()

    ls = [(i,int(v)) for i, v in enumerate(lns)]

    nl = [(i,int(v)) for i, v in enumerate(lns)]

##    zeroTerm  = 0
##    for i in range(len(ls)):
##        c = nl.index(ls[i])
##        if ls[i][1] == 0:
##            zeroTerm = ls[i]
##        v = nl.pop(c)
##        #print(c, v, c + v[1])
##        if (c + v[1] == 0):
##            nl.insert(len(nl), v)
##        else:
##            nl.insert((c + v[1])%len(nl), v)
##        #print([i[1] for i in nl])
##
##    zero = nl.index(zeroTerm)
##    print(zero)
##    print(nl[zero+1000][1]+nl[zero+2000][1]+nl[zero+3000][1])

    # Pt 2
    dec_key = 811589153
    #dec_key = 1

    ls = [(i,int(v)*dec_key) for i, v in enumerate(lns)]

    nl = [(i,int(v)*dec_key) for i, v in enumerate(lns)]

    length = len(nl)
    zeroTerm  = 0
    for i in range(10):
        for i in range(len(ls)):
            c = nl.index(ls[i])
            if ls[i][1] == 0:
                zeroTerm = ls[i]
            v = nl.pop(c)
            to = (c + v[1]) % (length-1)
            #print(c, v, c + v[1])
            if (to == 0):
                nl.insert(length, v)
            else:
                nl.insert(to, v)
            #print([i[1] for i in nl])

    zero = nl.index(zeroTerm)
    print(nl[zero+1000][1]+nl[zero+2000][1]+nl[zero+3000][1])
