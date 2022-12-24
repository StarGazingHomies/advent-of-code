import functools
import sys
import math
import time


def nicePrint(sizey, sizex, blizzards):
    printStrs = [list('#'*sizex)] + [list('#'+'.'*(sizex-2)+'#') for i in range(sizey-2)] + [list('#'*sizex)]
    for bx, by, bd in blizzards:
        if printStrs[bx][by] != '.':
            if printStrs[bx][by] in ('>','<','^','v'):
                printStrs[bx][by] = '2'
            elif printStrs[bx][by] == '#':
                print(printStrs)
            else:
                n = int(printStrs[bx][by])
                printStrs[bx][by] = str(n+1)
            continue
        if bd == (0,1):
            printStrs[bx][by] = '>'
        if bd == (0,-1):
            printStrs[bx][by] = '<'
        if bd == (-1,0):
            printStrs[bx][by] = '^'
        if bd == (1,0):
            printStrs[bx][by] = 'v'
    # Start
    printStrs[0][1] = '.'
    # End
    printStrs[-1][-2] = '.'
    newStr = ''
    for i in printStrs:
        for j in i:
            newStr += j
        newStr += '\n'
    print(newStr)

def nicePrint2(sizey, sizex, blizzards, moves):
    printStrs = [list('#'*sizex)] + [list('#'+'.'*(sizex-2)+'#') for i in range(sizey-2)] + [list('#'*sizex)]
    for bx, by, bd in blizzards:
        if printStrs[bx][by] != '.':
            if printStrs[bx][by] in ('>','<','^','v'):
                printStrs[bx][by] = '2'
            elif printStrs[bx][by] == '#':
                print(printStrs)
            else:
                n = int(printStrs[bx][by])
                printStrs[bx][by] = str(n+1)
            continue
        if bd == (0,1):
            printStrs[bx][by] = '>'
        if bd == (0,-1):
            printStrs[bx][by] = '<'
        if bd == (-1,0):
            printStrs[bx][by] = '^'
        if bd == (1,0):
            printStrs[bx][by] = 'v'
    for mt, mx, my in moves:
        printStrs[mx][my] = '!'
    # Start
    printStrs[0][1] = '.'
    # End
    printStrs[-1][-2] = '.'
    newStr = ''
    for i in printStrs:
        for j in i:
            newStr += j
        newStr += '\n'
    print(newStr)

def bfs(blizzardMoves, startT, startX, startY, endX, endY):
    global sizex, sizey
    steps = ((0,0),(1,0),(-1,0),(0,1),(0,-1))
    # BFS?
    # (time, posx, posy)
    l = [(startX, startY)]
    i = startT
    print(f"Doing a BFS from start {startT}, <{startX}, {startY}>...")
    while len(l)>0:
##        print(i)
##        nicePrint2(sizex, sizey, blizzardMoves[i], l)
        nl = []
        checkRepeat = [[False for i in range(130)] for i in range(30)]
        validMoves = [[True for i in range(130)] for i in range(30)]
        for bx, by, bd in blizzardMoves[i+1]:
            validMoves[bx][by] = False

        for x, y in l:
            for dx, dy in steps:
                # Valid?
                nx, ny = x+dx, y+dy
                if (nx == endX and ny == endY):
                    print(i+1)
                    return i+1
                if not ((1 <= nx <= sizex-2 and 1 <= ny <= sizey-2)
                        or (nx==startX and ny==startY)):
                    continue
                
                if validMoves[nx][ny]:
                    if not checkRepeat[nx][ny]:
                        nl.append((nx, ny))
                        checkRepeat[nx][ny] = True
        l = nl
##        print('-----------')
        i += 1
        if i%100 == 0:
            print(i, len(nl))
    print('???')
    return -1

def main():
    global sizex, sizey
    with open('24.in','r') as fin:
        lns = fin.readlines()

    dirMap = {'>':(0,1),
              '<':(0,-1),
              '^':(-1,0),
              'v':(1,0)}
    
    MOVES = 1000
    blizzards = []
    sizex = len(lns)
    sizey = len(lns[0])-1
    for i, ln in enumerate(lns):
        for j, c in enumerate(lns[i]):
            if c == '.' or c == '#' or c == '\n':
                continue
            blizzards.append((i,j,dirMap[c]))
##    print(blizzards)

    print("Grid size:", sizex, sizey)
    blizzardMoves = []
    blizzardMoves.append(blizzards.copy())
    print("Precalculating blizzard moves...")
    for i in range(MOVES):
##        nicePrint(sizex, sizey, blizzards)
        newBlizzards = []
        for bzdx, bzdy, bzdd in blizzards:
            nx = bzdx+bzdd[0]
            ny = bzdy+bzdd[1]
##            print(bzdx, bzdy, bzdd, nx, ny)
            if nx == sizex - 1:
                nx = 1
            if nx == 0:
                nx = sizex - 2
            if ny == sizey - 1:
                ny = 1
            if ny == 0:
                ny = sizey - 2
##            print('->', nx, ny)
            newBlizzards.append((nx, ny, bzdd))
        blizzards = newBlizzards
        blizzardMoves.append(blizzards)
        if i % 1000 == 0:
            print(i)

    t1 = bfs(blizzardMoves, 0, 0, 1, sizex-1, sizey-2)
    t2 = bfs(blizzardMoves, t1, sizex-1, sizey-2, 0, 1)
    t3 = bfs(blizzardMoves, t2, 0, 1, sizex-1, sizey-2)
    print(t1, t2, t3)
       
if __name__ == '__main__':
    main()
    
