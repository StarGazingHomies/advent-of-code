
if __name__ == '__main__':
    with open("8.in","r") as fin:
        lns = fin.readlines()

    grid = []
    for ln in lns:
        lineHeight = []
        for c in ln:
            if c == '\n':
                continue
            lineHeight.append(int(c))
        grid.append(lineHeight)

    # print(grid)

    # From the left
    left = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    for x in range(len(grid)):
        for y in range(1,len(grid[0])):
            left[x][y] = max(left[x][y-1], grid[x][y-1])

    right = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])-2, -1, -1):
            right[x][y] = max(right[x][y+1], grid[x][y+1])

    up = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    for y in range(len(grid[0])):
        for x in range(1, len(grid)):
            up[x][y] = max(up[x-1][y], grid[x-1][y])

    down = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    for y in range(len(grid[0])):
        for x in range(len(grid)-2, -1, -1):
            down[x][y] = max(down[x+1][y], grid[x+1][y])

    coverage = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    cnt = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            coverage[x][y] = min(left[x][y], right[x][y], up[x][y], down[x][y])
            if coverage[x][y] < grid[x][y]:
                cnt += 1
    print(cnt)

    # Part 2
    # Nah just gonna go with something O(m^2n^2) in worst circumstance
    maxScenicScore = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            # Go left
            z = y-1
            rightScore = 0
            while (z >= 0 and grid[x][z] < grid[x][y]):
                rightScore += 1
                z -= 1
            # The massive tree that you can see still counts
            if (z >= 0):
                rightScore += 1

            z = y+1
            leftScore = 0
            while (z < len(grid[0]) and grid[x][z] < grid[x][y]):
                leftScore += 1
                z += 1
            if (z < len(grid[0])):
                leftScore += 1

            z = x-1
            upScore = 0
            while (z >= 0 and grid[z][y] < grid[x][y]):
                upScore += 1
                z -= 1
            if (z >= 0):
                upScore += 1

            z = x+1
            downScore = 0
            while (z < len(grid) and grid[z][y] < grid[x][y]):
                downScore += 1
                z += 1
            if (z < len(grid[0])):
                downScore += 1

            maxScenicScore = max(maxScenicScore, upScore * downScore * leftScore * rightScore)
            # print(x, y, grid[x][y], rightScore, leftScore, upScore, downScore)
    print(maxScenicScore)
