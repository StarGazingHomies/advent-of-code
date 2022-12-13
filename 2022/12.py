DIRECTIONS = [(0,-1), (-1,0), (0,1), (1,0)]

def bfs(grid, starts):
    global err
    # Based on AOC thread in Manechat... literally bfs is enough lmao
    pos = starts
    vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cnt = 0
    while len(pos) > 0:
        newPos = []
        for x, y in pos:
            if vis[x][y]:
                continue
            vis[x][y] = True

            if grid[x][y] == 'E':
                return cnt
            
            curVal = ord(grid[x][y])
            if curVal == ord('S'):
                curVal = ord('a')

            # If you can go somewhere
            if x >= 1               and curVal >= (ord('y') if grid[x-1][y] == 'E' else ord(grid[x-1][y]) - 1)  and (x-1,y) not in vis:
                newPos.append((x-1,y))
            if x < len(grid) - 1    and curVal >= (ord('y') if grid[x+1][y] == 'E' else ord(grid[x+1][y]) - 1) and (x+1,y) not in vis:
                newPos.append((x+1,y))
            if y >= 1               and curVal >= (ord('y') if grid[x][y-1] == 'E' else ord(grid[x][y-1]) - 1)  and (x,y-1) not in vis:
                newPos.append((x,y-1))
            if y < len(grid[0]) - 1 and curVal >= (ord('y') if grid[x][y+1] == 'E' else ord(grid[x][y+1]) - 1) and (x,y+1) not in vis:
                newPos.append((x,y+1))

        pos = newPos
        cnt += 1
    # Something prolly went wrong
    return -1

if __name__ == '__main__':
    with open("12.in","r") as fin:
        lns = fin.readlines()
    
    # Part 1
    starts = []
    for i,ln in enumerate(lns):
        for x,c in enumerate(ln):
            if c == 'S':
                starts.append((i,x))

    print(bfs(lns, starts))

    # Part 2
    starts = []
    for i,ln in enumerate(lns):
        for x,c in enumerate(ln):
            if c == 'S' or c == 'a':
                starts.append((i,x))

    print(bfs(lns, starts))
