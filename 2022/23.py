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

def nicePrint(grid):
    printStr = ''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                printStr += '.'
            else:
                printStr += '#'
        printStr += '\n'
    print(printStr)

def nicePrintHighlight(grid, posx, posy):
    printStr = ''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i==posy and j==posx):
                printStr += '!'
            elif grid[i][j] == 0:
                printStr += '.'
            else:
                printStr += '#'
        printStr += '\n'
    print(printStr)

def nicePrint2(grid, moveTo):
    printStr = ''
    newGrid = [grid[i].copy() for i in range(len(grid))]
    for m in moveTo:
        ox, oy, nx, ny = m
        d = (nx-ox, ny-oy)
        if d == (1,0):
            newGrid[oy][ox] = '>'
        if d == (-1,0):
            newGrid[oy][ox] = '<'
        if d == (0,-1):
            newGrid[oy][ox] = '^'
        if d == (0,1):
            newGrid[oy][ox] = 'v'
            
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if newGrid[i][j] == 0:
                printStr += '.'
            elif newGrid[i][j] == 1:
                printStr += '#'
            else:
                printStr += str(newGrid[i][j])
        printStr += '\n'
    print(printStr)

if __name__ == '__main__':
    with open('23.in','r') as fin:
        lns = fin.readlines()

    PADDING = 100
    grid = [[0 for i in range(PADDING*2+len(lns[0]))] for i in range(PADDING)]
    for ln in lns:
        tmpLn = [0 for i in range(PADDING)]
        for c in ln:
            if c == '.':
                tmpLn.append(0)
            elif c == '\n':
                continue
            else:
                tmpLn.append(1)
        tmpLn += [0 for i in range(PADDING)]
        grid.append(tmpLn)

    grid += [[0 for i in range(PADDING*2+len(lns[0]))] for i in range(PADDING)]
    

    moveDirs = [(( 0,-1), ( 1,-1), (-1,-1)),
                (( 0, 1), ( 1, 1), (-1, 1)),
                ((-1, 0), (-1, 1), (-1,-1)),
                (( 1, 0), ( 1, 1), ( 1,-1))]
    hasElvesAround = [(-1,0), (-1,-1), (0,-1), (1,-1),
                      (1,0), (1,1), (0,1), (-1,1)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                elfPos.append((y,x))
    
    for rnd in range(1000):
        moveTo = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    continue

##                print("Elf at:", x, y)
                for d in hasElvesAround:
                    if grid[y+d[1]][x+d[0]] != 0:
                        break
                else:
##                    print("Elf has no other elves around!")
                    continue
                
##                nicePrintHighlight(grid, x, y)
##                elfDebugStr = ''
                for di, ds in enumerate(moveDirs):
##                    elfDebugStr += f"Checking direction: {di}, {ds}\n"
                    for d in ds:
                        if grid[y+d[1]][x+d[0]] != 0:
##                            elfDebugStr += f"Another elf at: {x+d[0]}, {y+d[1]}\n"
                            break
                    else:
##                        elfDebugStr += f"Proposes to move in {ds[0]}\n"
                        moveTo.append((x,y,x+ds[0][0],y+ds[0][1]))
                        break
##                print(elfDebugStr+"------")
                
##        print(moveTo)
        removes = []
        for i, elf1 in enumerate(moveTo):
            for j, elf2 in enumerate(moveTo[:i]):
                if elf1[2]==elf2[2] and elf1[3] == elf2[3]:
                    removes.append(i)
                    removes.append(j)
##                    print(i,j)
        removes.sort()
        lastrmv = -1
##        print(removes)
        for i in range(len(removes)-1,-1,-1):
            rmv = removes[i]
##            print(rmv, lastrmv)
            if rmv == lastrmv:
                continue
            moveTo.pop(rmv)
            lastrmv = rmv

        if len(moveTo) == 0:
            print("No elf moved!", rnd+1)
            break
##        print(moveTo)
##        nicePrint2(grid,moveTo)
        for move in moveTo:
            ox, oy, nx, ny = move
            grid[oy][ox] = 0
            grid[ny][nx] = 1
        
##        nicePrint(grid)
        moveDirs.append(moveDirs.pop(0))
##        input()
        if rnd%100==0:
            print(rnd)

    minElfx, minElfy, maxElfx, maxElfy = 1000,1000,-1,-1
    elfCnt = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                elfCnt += 1
                minElfx = min(x,minElfx)
                maxElfx = max(x,maxElfx)
                minElfy = min(y,minElfy)
                maxElfy = max(y,maxElfy)
    print((maxElfy-minElfy+1)*(maxElfx-minElfx+1)-elfCnt)
