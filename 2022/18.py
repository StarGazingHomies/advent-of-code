import functools
import sys

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

LEN = 21
def color(grid):
    pos = [(1,1,1)]
    while len(pos) > 0:
        cx, cy, cz = pos.pop(-1)
        if grid[cx][cy][cz] == 2:
            continue
        grid[cx][cy][cz] = 2
        
        for dx, dy, dz in ((0,0,1), (0,0,-1), (1,0,0), (-1,0,0), (0,1,0), (0,-1,0)):
            nx, ny, nz = cx-dx, cy-dy, cz-dz
            if 0 <= nx < LEN and 0 <= ny < LEN and 0 <= nz < LEN:
                if grid[nx][ny][nz] == 0:
                    pos.append((nx, ny, nz))
        #print(cx,cy,cz)
    return grid

def niceprint(grid):
    for x in range(LEN):
        for y in range(LEN):
            for z in range(LEN):
                print(grid[x][y][z], end='')
            print()
        print('--------------------')

if __name__ == '__main__':
    with open('18.in','r') as fin:
        lns = fin.readlines()

    print(len(lns))

    droplets = []
    for ln in lns:
        d = ln.split(',')
        x,y,z = int(d[0]), int(d[1]), int(d[2])
        droplets.append((x,y,z))

    a = 0
    print((1,1,1) in droplets)
    grid = [[[0 for i in range(LEN)] for i in range(LEN)] for i in range(LEN)]
    
    for d in droplets:
        dx, dy, dz = d
        a += 6
        grid[dx][dy][dz] = 1

    #niceprint(grid)
    grid = color(grid)
    #niceprint(grid)
    #print(grid[2][2][5])
    a = 0
    for dx, dy, dz in droplets:
        if grid[dx+1][dy][dz] == 2:
            a += 1
        if grid[dx-1][dy][dz] == 2:
            a += 1
        if grid[dx][dy+1][dz] == 2:
            a += 1
        if grid[dx][dy-1][dz] == 2:
            a += 1
        if grid[dx][dy][dz+1] == 2:
            a += 1
        if grid[dx][dy][dz-1] == 2:
            a += 1


    print(a)
