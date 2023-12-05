def main():
    with open('4.in', 'r') as f:
        lines = f.readlines()

    total = 0
    curCards = [1 for i in range(len(lines))]
    cardResults = []
    for index, line in enumerate(lines):
        trim = line.split(':')[1]
        front, back = trim.split('|')
        match = []
        r = -1
        for i in front.split(' '):
            if i == '':
                continue
            match.append(int(i))

        for i in back.split(' '):
            if i == '':
                continue
            if int(i) in match:
                r += 1

        if r != -1:
            for j in range(index+1, index+r+2):
                curCards[j] += curCards[index]

        # if r != -1:
        #     cardResults.append([i+j for j in range(r+1)])
        # else:
        #     cardResults.append([])
    print(sum(curCards))


if __name__ == '__main__':
    main()
