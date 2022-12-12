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

if __name__ == '__main__':
    with open("12.in","r") as fin:
        lns = fin.readlines()
    
    start = 0
    goal = 0
    
    grid = [[] for i in range(len(lns))]
    starts = []
    for i,ln in enumerate(lns):
        for x,c in enumerate(ln):
            if c == '\n':
                continue
            elif c == 'S':
                grid[i].append(0)
                start = (i*160+ln.index('S'))
                starts.append(i*160 + x)
            elif c == 'E':
                grid[i].append(ord('z')-ord('a'))
                goal = (i*160+ ln.index('E'))
            elif c == 'a':
                grid[i].append(0)
                starts.append(i*160 + x)
            else:
                grid[i].append(ord(c)-ord('a'))


    print(len(grid), len(grid[i]))
    print(grid)

    paths = [[] for i in range(160*50)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            index = i*160+j
            
            # Iterate each tile
            try:
                if grid[i][j-1] - grid[i][j] <= 1:
                    paths[index].append(i*160+j-1)
            except IndexError:
                pass
            try:
                if grid[i][j+1] - grid[i][j] <= 1:
                    paths[index].append(i*160+j+1)
            except IndexError:
                pass

            try:
                if grid[i-1][j] - grid[i][j] <= 1:
                    paths[index].append(i*160+j-160)
            except IndexError:
                pass

            try:
                if grid[i+1][j] - grid[i][j] <= 1:
                    paths[index].append(i*160+j+160)
            except IndexError:
                pass

    print(paths[start])

    totlen = 0

    with open("12_interim.in","w") as fout:
        for i, n in enumerate(paths):
            for m in n:
                totlen += 1
                fout.write(f"{i} {m} 1\n")
