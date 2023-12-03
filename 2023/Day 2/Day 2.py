RED = 12
BLUE = 14
GREEN = 13


def part1(usefulInfo: str):
    possible = True
    for draw in usefulInfo:
        ballTypes = draw.split(",")
        for t in ballTypes:
            _, num, color = t.split(' ')
            color = color.replace("\n", "")
            num = int(num)
            if color == 'red' and num > RED:
                possible = False
                break
            elif color == 'blue' and num > BLUE:
                possible = False
                break
            elif color == 'green' and num > GREEN:
                possible = False
                break
        if not possible:
            break
    if possible:
        return True
    return False


def Part2(usefulInfo: str):
    maxRed, maxBlue, maxGreen = 0, 0, 0
    for draw in usefulInfo:
        ballTypes = draw.split(",")
        for t in ballTypes:
            _, num, color = t.split(' ')
            color = color.replace("\n", "")
            num = int(num)
            if color == 'red':
                maxRed = max(maxRed, num)
            elif color == 'blue':
                maxBlue = max(maxBlue, num)
            elif color == 'green':
                maxGreen = max(maxGreen, num)
    return maxRed * maxBlue * maxGreen

def main():
    with open("2.in", "r") as f:
        lines = f.readlines()

    total = 0
    for i, line in enumerate(lines):
        usefulInfo = line.split(":")[1]
        usefulInfo = usefulInfo.split(";")
        total += Part2(usefulInfo)

    print(total)


if __name__ == '__main__':
    main()