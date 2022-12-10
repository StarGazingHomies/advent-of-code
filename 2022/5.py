if __name__ == '__main__':
    # Part 1
    with open('5.in','r') as fin:
        lns = fin.readlines()

    # Crate input
    curBoxes = [ [] for i in range(10) ]
    for lineNumber in range(7,-1,-1):
        ln = lns[lineNumber]
        for column in range(1,36,4):
            if (ln[column] != ' '):
                curBoxes[column//4+1].append(ln[column])

    # Moves
    for ln in lns[10:]:
        amount = int(ln[5:ln.index(" from ")])
        src = int(ln[ln.index(" from ") + 6:ln.index(" to ")])
        dst = int(ln[ln.index(" to ") + 4:])

        for i in range(amount):
            curBoxes[dst].append(curBoxes[src].pop(-1))

    for stack in curBoxes[1:]:
        print(stack[-1], end='')

    # Part 2
    with open('5.in','r') as fin:
        lns = fin.readlines()

    # Crate input
    curBoxes = [ [] for i in range(10) ]
    for lineNumber in range(7,-1,-1):
        ln = lns[lineNumber]
        for column in range(1,36,4):
            if (ln[column] != ' '):
                curBoxes[column//4+1].append(ln[column])

    # Moves
    for ln in lns[10:]:
        amount = int(ln[5:ln.index(" from ")])
        src = int(ln[ln.index(" from ") + 6:ln.index(" to ")])
        dst = int(ln[ln.index(" to ") + 4:])

        stack = []
        for i in range(amount):
            stack.append(curBoxes[src].pop(-1))
        for i in range(amount):
            curBoxes[dst].append(stack.pop(-1))

    print()
    for stack in curBoxes[1:]:
        print(stack[-1], end='')
