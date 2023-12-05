def main():
    with open('5.in', 'r') as f:
        lines = f.readlines()

    seeds = [int(i) for i in lines[0][7:].split(' ')]
    mapped = [False for i in range(len(seeds))]

    maps = []
    curMap = []
    for line in lines[2:]:
        if line == '\n':
            maps.append(curMap)
            curMap = []
        else:
            curMap.append(line)
    maps.append(curMap)

    print(seeds)
    for map in maps:
        mapped = [False for i in range(len(seeds))]
        # LastStart, ThisStart, Range
        for m in map[1:]:
            thisStart, lastStart, Range = [int(i) for i in m.split(' ')]

            for i, seed in enumerate(seeds):
                if mapped[i]:
                    continue
                if 0 <= (seed - lastStart) < Range:
                    # Replace
                    seeds[i] = thisStart + (seed - lastStart)
                    mapped[i] = True
        # print(seeds)
    print(min(seeds))


def performMap(range, map):
    results = [(range[0], range[1], False)]
    for thisStart, lastStart, Range in map:
        # Change lastStart ~ lastStart + range to thisStart ~ thisStart + range
        lastEnd = lastStart + Range
        delta = thisStart - lastStart
        for i, result in enumerate(results):
            if result[2]:
                continue
            # Encompass
            if lastStart <= result[0] and result[1] <= lastEnd:
                results[i] = (result[0] + delta, result[1] + delta, True)
            # Left
            elif lastStart <= result[0] < lastEnd:
                results[i] = (result[0] + delta, lastEnd + delta, True)
                results.append((lastEnd, result[1], False))
            # Right
            elif lastStart < result[1] <= lastEnd:
                results[i] = (lastStart + delta, result[1] + delta, True)
                results.append((result[0], lastStart, False))
            # Inside
            elif result[0] < lastStart <= lastEnd < result[1]:
                results[i] = (lastStart + delta, lastEnd + delta, True)
                results.append((result[0], lastStart, False))
                results.append((lastEnd, result[1], False))
            # Outside
            else:
                continue
    return [(result[0], result[1]) for result in results]


def main2():
    with open('5.in', 'r') as f:
        lines = f.readlines()

    seeds = [int(i) for i in lines[0][7:].split(' ')]
    # Pair seeds into ranges
    seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    mapped = [False for i in range(len(seeds))]

    maps = []
    curMap = []
    for line in lines[2:]:
        if line == '\n':
            maps.append(curMap)
            curMap = []
        else:
            curMap.append(line)
    maps.append(curMap)

    for i, map in enumerate(maps):
        betterMap = []
        for m in map[1:]:
            thisStart, lastStart, Range = [int(i) for i in m.split(' ')]
            betterMap.append((thisStart, lastStart, Range))
        map = betterMap
        maps[i] = map
        # print(map)
        newSeeds = []
        for seed in seeds:
            newSeeds += performMap(seed, map)
        print(newSeeds)
        seeds = newSeeds

    print(min([seed[0] for seed in seeds]))

if __name__ == '__main__':
    main2()