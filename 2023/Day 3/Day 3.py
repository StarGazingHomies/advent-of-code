def getInts(line):
    # Isolate numbers from the lines
    i = []
    cur = 0
    for c in line:
        if c.isdigit():
            cur *= 10
            cur += int(c)
        else:
            i.append(cur)
            cur = 0
    if cur != 0:
        i.append(cur)
    return i


def isSymbol(char):
    return char != "." and char != "\n" and (char < "0" or char > "9")


part = 2

def getNumAt(lines, i, j):
    # Go backward
    n = f"{lines[i][j]}"
    for k in range(j-1, -1, -1):
        if lines[i][k].isdigit():
            n = f"{lines[i][k]}{n}"
            # print(k, n)
        else:
            break
    # Go forward
    for k in range(j+1, len(lines[i])):
        if lines[i][k].isdigit():
            n = f"{n}{lines[i][k]}"
            # print(k, n)
        else:
            break
    return int(n)


def main():
    global part
    with open("3.in", "r") as f:
        lines = f.readlines()

    if part == 1:
        total = 0
        for i in range(len(lines)):
            # Isolate numbers from the lines
            nums = getInts(lines[i])
            j = 0
            for n in nums:
                newJ = j + len(str(n)) + 1
                if n == 0:
                    j = newJ - 1
                    continue
                print(n, i, j, newJ)
                hasSymbol = False
                # Check top and bottom
                for k in range(j-1, newJ):
                    try:
                        print("top", i-1, k)
                        if i > 0 and isSymbol(lines[i - 1][k]):
                            hasSymbol = True
                            break
                        print("bottom", i+1, k)
                        if i < len(lines) - 1 and isSymbol(lines[i + 1][k]):
                            hasSymbol = True
                            break
                    except IndexError:
                        pass
                # Check left and right
                print("left", i, j-1)
                if j > 0 and isSymbol(lines[i][j - 1]):
                    hasSymbol = True
                print("right", i, newJ-1)
                if newJ < len(lines[i]) and isSymbol(lines[i][newJ-1]):
                    hasSymbol = True
                print(n, hasSymbol)
                if hasSymbol:
                    total += n
                j = newJ
                print("------")
        print(total)

    if part == 2:
        # Find all '*' symbols
        total = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != '*':
                    continue

                # Find numbers around this *
                nums = []
                # Try top
                x = j - 1
                while x <= j + 1:
                    try:
                        print(i-1, x, lines[i-1][x])
                        if 0 <= x <= len(lines[i-1]) and lines[i-1][x].isdigit():
                            nums.append(getNumAt(lines, i-1, x))
                            while lines[i-1][x].isdigit():
                                x += 1
                    except IndexError:
                        pass
                    finally:
                        x += 1
                # Try bottom
                x = j - 1
                while x <= j + 1:
                    try:
                        print(i+1, x, lines[i+1][x])
                        if 0 <= x <= len(lines[i+1]) and lines[i+1][x].isdigit():
                            nums.append(getNumAt(lines, i+1, x))
                            while lines[i+1][x].isdigit():
                                x += 1
                    except IndexError:
                        pass
                    finally:
                        x += 1
                # Try left
                print(i, j-1, lines[i][j-1])
                if j > 0 and lines[i][j-1].isdigit():
                    nums.append(getNumAt(lines, i, j-1))
                # Try right
                print(i, j+1, lines[i][j+1])
                if j < len(lines[i]) and lines[i][j+1].isdigit():
                    nums.append(getNumAt(lines, i, j+1))
                print(nums)
                if len(nums) == 2:
                    print(nums[0] * nums[1])
                    total += nums[0] * nums[1]
        print(total)




if __name__ == '__main__':
    main()
