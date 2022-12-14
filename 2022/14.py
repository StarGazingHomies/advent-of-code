def ints(line):
    i = 0
    rtrns = []
    while i < len(line):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0']:
            j = i + 1
            while j < len(line) and line[j] in ['1','2','3','4','5','6','7','8','9','0']:
                j += 1
            
            rtrns.append(int(line[i:j]))
            i = j
        i += 1
    return rtrns

def spawnSand(grid):
    px, py = 500, 0

    if grid[px][py] != 0:
        return -1, -1

    try:
        while (py != 999):
##            print(px, py)
            if grid[px][py+1] == 0:
                py += 1
                continue
            if grid[px-1][py+1] == 0:
                px -= 1
                py += 1
                continue
            if grid[px+1][py+1] == 0:
                px += 1
                py += 1
                continue
            
            return px, py
    except IndexError:
##        print(px, py)
        return -1, -1

    return -1, -1
            
if __name__ == '__main__':
    with open('14.in','r') as fin:
        lns = fin.readlines()

    grid = [[0 for i in range(1000)] for i in range(1000)]

    lowestY = 0

    for ln in lns:
        its = ints(ln)
        for i in range(0, len(its)-2, 2):
            x1 = its[i]
            y1 = its[i+1]
            x2 = its[i+2]
            y2 = its[i+3]
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            if (x1 == x2):
                for y in range(y1, y2+1):
                    grid[x1][y] = 1
            else:
                for x in range(x1, x2+1):
                    grid[x][y1] = 1
            lowestY = max(lowestY, y2)

    # Remove for loop for pt1
    for i in range(0, 1000):
        grid[i][lowestY+2] = 1
    
    cnt = 0
    while True:
        px, py = spawnSand(grid)
        if (px == -1 and py == -1):
            break
        #print(cnt, px, py)
        grid[px][py] = 2
        cnt += 1
    print("Part 2:", cnt)

    
