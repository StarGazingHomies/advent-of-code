MAX_COORDINATE = 100000

def getDir(a, b):
    if (a==b):
        return 0
    return int(abs(a-b)/(a-b))

def moveTail(head, tail):
    # No need to move
    if abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
        return [0,0]
    return [getDir(head[0], tail[0]), getDir(head[1], tail[1])]

def getDirection(char):
    if (char == 'U'):
        return [0,1]
    if (char == 'R'):
        return [1,0]
    if (char == 'D'):
        return [0,-1]
    if (char == 'L'):
        return [-1,0]
    else:
        print("Invalid input!")

def posHash(pos):
    return pos[0]*MAX_COORDINATE*2+pos[1]+MAX_COORDINATE

def debugPart2(knots):
    for i in range(5,-5,-1):
        for j in range(-5,5,1):
            if [j,i] in knots:
                print(knots.index([j,i]), end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    head = [0,0]
    tail = [0,0]

    visited = {}

    with open('9.in','r') as fin:
        lns = fin.readlines()

    # Part 1
    for ln in lns:
        dirChar, moves = ln.split(' ')
        direction = getDirection(dirChar)
        moves = int(moves)
        for i in range(moves):
            head[0] += direction[0]
            head[1] += direction[1]

            tailMoves = moveTail(head, tail)

            tail[0] += tailMoves[0]
            tail[1] += tailMoves[1]

            #print(head, tail)
            visited[posHash(tail)] = True
    
    print(len(visited.keys()))

    # Part 2
    numOfKnots = 10
    knots = [[0,0] for i in range(numOfKnots)]
    visited = {}
    
    for ln in lns:
        dirChar, moves = ln.split(' ')
        originalDirection = getDirection(dirChar)
        moves = int(moves)
        # print(direction, moves)
        for i in range(moves):
            direction = originalDirection
            for i in range(numOfKnots):
                # print(i, direction)
                knots[i][0] += direction[0]
                knots[i][1] += direction[1]
                if (i < numOfKnots - 1):
                    direction = moveTail(knots[i], knots[i+1])
            
            visited[posHash(knots[numOfKnots-1])] = True

        #debugPart2(knots)

    print(len(visited.keys()))
