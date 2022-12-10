if __name__ == '__main__':
    with open('1.in','r') as fin:
        lns = fin.readlines();

    foods = []
    c = 0
    for ln in lns:
        if (ln == '\n'):
            foods.append(c)
            c = 0
            continue
        c += int(ln)
    foods.sort()
    # Part 1
    print(foods[-1])
    # Part 2
    print(sum(foods[-1:-4:-1]))
