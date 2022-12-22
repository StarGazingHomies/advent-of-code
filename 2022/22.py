import functools
import sys
import math
import time
import random

def parse(line):
    i = 0
    rtrns = []
    while i < len(line):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0']:
            j = i + 1
            while j < len(line) and line[j] in ['1','2','3','4','5','6','7','8','9','0']:
                j += 1
            
            rtrns.append(int(line[i:j]))
            rtrns.append(line[j:j+1])
            i = j
        i += 1
    return rtrns[:-1]

def nicePrint(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(end=str(grid[i][j]))
        print()
def nicePrint2(grid):
    for fr in range(0,len(grid),3):
        print(f"Face {fr} - {fr+2}:")
        m = ['' for i in range(len(grid[fr]))]
        for f in range(fr,fr+3):
            for i in range(len(grid[f])):
                for j in range(len(grid[f][i])):
                    m[i] += grid[f][i][j]
                m[i] += ' | '
        for i in range(len(grid[fr])):
            print(m[i])
        print()

def warpAround(grid, x, y, d):
    if d == [1,0]:
        x = 0
        while grid[y][x] == ' ':
            x += 1
        return x, y
    if d == [0,1]:
        y = 0
        while grid[y][x] == ' ':
            y += 1
        return x, y
    if d == [-1,0]:
        x = len(grid[y])-1
        while grid[y][x] == ' ':
            x -= 1
        return x, y
    if d == [0,-1]:
        y = len(grid)-1
        while grid[y][x] == ' ':
            y -= 1
        return x, y

CUBESIZE = 50
def ThreeDCube(grid, x, y, d):
    # Fuck me why did I do this
    if y == CUBESIZE*2 and 0 <= x < CUBESIZE:
        return CUBESIZE*3-1-x, CUBESIZE*3-1, [0,-1]
    if CUBESIZE*2 <= x < CUBESIZE*3 and y == CUBESIZE * 3:
        return CUBESIZE*3-1-x, CUBESIZE*2-1, [0,-1]
    
    if y == CUBESIZE*2 and CUBESIZE <= x < CUBESIZE*2 and d == [0,1]:
        return CUBESIZE*2, CUBESIZE*4-1-x, [1,0]
    if x == CUBESIZE*2-1 and CUBESIZE*2 <= y < CUBESIZE*3 and d == [-1,0]:
        return CUBESIZE*4-1-y, CUBESIZE*2-1, [0,-1]
    
    
    if x == -1 and CUBESIZE <= y < CUBESIZE*2:
        return CUBESIZE*5-1-y, CUBESIZE*3-1, [0, -1]
    if CUBESIZE*3 <= x < CUBESIZE*4 and y == CUBESIZE * 3:
        return 0, CUBESIZE*5-1-x, [1,0]

    if x == 4*CUBESIZE and CUBESIZE * 2 <= y < CUBESIZE * 3:
        return 3*CUBESIZE-1, 3*CUBESIZE-1-y, [-1,0]
    if x == 3*CUBESIZE and 0 <= y < CUBESIZE:
        return 4*CUBESIZE-1, 3*CUBESIZE-1-y, [-1,0]

    if x == 3*CUBESIZE and CUBESIZE <= y < CUBESIZE*2 and d == [1,0]:
        return 5*CUBESIZE-1-y,2*CUBESIZE, [0,1]
    if 3*CUBESIZE <= x < 4*CUBESIZE and y == 2*CUBESIZE-1 and d == [0,-1]:
        return 3*CUBESIZE-1, 5*CUBESIZE-1-x, [-1,0]

    if y == CUBESIZE-1 and CUBESIZE <= x < CUBESIZE*2 and d == [0,-1]:
        return CUBESIZE*2, x-CUBESIZE, [1,0]
    if x == 2*CUBESIZE-1 and 0 <= y < CUBESIZE and d == [-1,0]:
        return y+CUBESIZE, CUBESIZE, [0,1]
    
    if y == CUBESIZE-1 and 0 <= x < CUBESIZE:
        return CUBESIZE*3-1-x, 0, [0,1]
    if y == -1 and 2*CUBESIZE <= x < 3*CUBESIZE:
        return CUBESIZE*3-1-x, CUBESIZE, [0,1]

    print(x,y,d, '!!!')


def switchFace(faces, face, x, y, d):
    c = CUBESIZE-1
    goToChart = [[],
                 # 1
                 [[2,['0','y'],[1,0]],
                  [3,['x','0'],[0,1]],
                  [4,['0','c-y'],[1,0]],
                  [6,['0','x'],[1,0]]],
                 # 2
                 [[5,['c','c-y'],[-1,0]],
                  [3,['c','x'],[-1,0]],
                  [1,['c','y'],[-1,0]],
                  [6,['x','c'],[0,-1]]],
                 # 3
                 [[2,['y','c'],[0,-1]],
                  [5,['x','0'],[0,1]],
                  [4,['y','0'],[0,1]],
                  [1,['x','c'],[0,-1]]],
                 # 4
                 [[5,['0','y'],[1,0]],
                  [6,['x','0'],[0,1]],
                  [1,['0','c-y'],[1,0]],
                  [3,['0','x'],[1,0]]],
                 # 5
                 [[2,['c','c-y'],[-1,0]],
                  [6,['c','x'],[-1,0]],
                  [4,['c','y'],[-1,0]],
                  [3,['x','c'],[0,-1]]],
                 # 6
                 [[5,['y','c'],[0,-1]],
                  [2,['x','0'],[0,1]],
                  [1,['y','0'],[0,1]],
                  [4,['x','c'],[0,-1]]]]

    if d == [1,0]:
        dnum = 0
    elif d == [0,1]:
        dnum = 1
    elif d == [-1,0]:
        dnum = 2
    elif d == [0,-1]:
        dnum = 3
    else:
        print("!!!!!????")

##    print(face)
    goTo = goToChart[face+1][dnum]
##    print(x, y, goTo, c)
##    print(goTo[0]-1, eval(goTo[1][0]), eval(goTo[1][1]), goTo[2])
##    
    return goTo[0]-1, eval(goTo[1][0]), eval(goTo[1][1]), goTo[2]
    
if __name__ == '__main__':
    with open('22.in','r') as fin:
        lns = fin.readlines()

    grid = [ln[:-1]+' ' for ln in lns[:-2]]

    steps = parse(lns[-1])
    #print(steps)
    #nicePrint(grid)
    posx = grid[0].index('.')
    posy = 0
    direction = [1,0]
    #print("Start:", posx, posy, direction)

##    for s in steps:
##        if type(s) == int:
##            for i in range(s):
##                posx += direction[0]
##                posy += direction[1]
##                try:
##                    if grid[posy][posx] == '#':
##                        posx -= direction[0]
##                        posy -= direction[1]
##                        break
##                except IndexError:
##                    posx, posy = warpAround(grid, posx, posy, direction)
##                    continue
##                if grid[posy][posx] == ' ':
##                    posx, posy = warpAround(grid, posx, posy, direction)
##                #print(posx, posy, direction)
##        elif type(s) == str:
##            if s == 'L':
##                direction = [direction[1], -direction[0]]
##            if s == 'R':
##                direction = [-direction[1], direction[0]]
##        #print(posx, posy, direction)
##
##    password = 1000*(posy+1) + 4*(posx+1)
##    if direction == [1,0]:
##        password += 0
##    if direction == [0,1]:
##        password += 1
##    if direction == [-1,0]:
##        password += 2
##    if direction == [0,-1]:
##        password += 3
##    print(password)

    # Part 2
    
    posx = 0
    posy = 0
    faceID = 0
    direction = [1,0]
    #print("Start:", posx, posy, direction)

    faces = []
    newFaces = []
    faceLocation = []
    for i in range(0,len(grid),CUBESIZE):
        for j in range(0,len(grid[i]),CUBESIZE):
            if grid[i][j] != ' ':
                faceGrid = [grid[k][j:j+CUBESIZE] for k in range(i,i+CUBESIZE)]
##                faceGrid = ['.'*50 for k in range(i,i+CUBESIZE)]
                faces.append(faceGrid)
                
                newFaceGrid = [list(grid[k][j:j+CUBESIZE]) for k in range(i,i+CUBESIZE)]
##                newFaceGrid = [['.']*50 for k in range(i,i+CUBESIZE)]
                newFaces.append(newFaceGrid)
                faceLocation.append((i,j))
    
    #newGrid = [list(i) for i in grid]

    for s in steps:
        if type(s) == int:
##            s = random.randint(60,120)
            for i in range(s):
##                try:
##                print(faceID, posy, posx)
                if direction == [1,0]:
                    newFaces[faceID][posy][posx] = '>'
                if direction == [0,1]:
                    newFaces[faceID][posy][posx] = 'v'
                if direction == [-1,0]:
                    newFaces[faceID][posy][posx] = '<'
                if direction == [0,-1]:
                    newFaces[faceID][posy][posx] = '^'
##                except Exception:
##                    pass
##                finally:
##                    nicePrint2(newFaces)
##                    print('--------------------------')
                oF, oX, oY, oD = faceID, posx, posy, direction.copy()
                
                posx += direction[0]
                posy += direction[1]

                if not (0 <= posx < CUBESIZE and 0 <= posy < CUBESIZE):
                    faceID, posx, posy, direction = switchFace(faces, faceID, oX, oY, direction)

##                print("size", len(faces[faceID]),len(faces[faceID][0]))
                if faces[faceID][posy][posx] == '#':
                    faceID, posx, posy, direction = oF, oX, oY, oD
                    break
                #print(posx, posy, direction)

        elif type(s) == str:
##            s = random.randint(0,1)
            if s == 0:
                s = 'L'
            if s == 1:
                s = 'R'
                
            if s == 'L':
                direction = [direction[1], -direction[0]]
            if s == 'R':
                direction = [-direction[1], direction[0]]
##        print(faceID, posx, posy, direction)
##        nicePrint2(newFaces)
##        print('--------------------------')
##        input()

##    nicePrint(newGrid)
##    print(faceLocation)
    i, j = faceLocation[faceID]
    posx += j
    posy += i
    password = 1000*(posy+1) + 4*(posx+1)
    if direction == [1,0]:
        password += 0
    if direction == [0,1]:
        password += 1
    if direction == [-1,0]:
        password += 2
    if direction == [0,-1]:
        password += 3
    print(password)
