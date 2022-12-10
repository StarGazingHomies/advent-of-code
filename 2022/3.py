def letterToPriority(l):
    n = ord(l)
    if ord('a') <= n <= ord('z'):
        return n-ord('a')+1
    elif ord('A') <= n <= ord('Z'):
        return n-ord('A')+27
    else:
        raise Exception(str(l) + " is not a valid priority!")

def priorityToLetter(p):
    if (1<=p<=26):
        return chr(p+ord('a'))
    elif (27 <= p <= 52):
        return chr(p+ord('A')-26)
    else:
        raise Exception(str(p) + " is not a valid priority!")

def lineToLetter(ln):
    firstHalf, secondHalf = ln[:len(ln)//2], ln[len(ln)//2:]
    #print(firstHalf, secondHalf)
    existingLetters = {}
    for l in firstHalf:
        existingLetters[l] = True
    #print(existingLetters)
    for l in secondHalf:
        if l not in existingLetters.keys():
            continue
        if existingLetters[l]:
            #print(l)
            return l
    raise Exception(ln + " is not a valid line!")

def findCommonLetter_Part2(lines):
    existence = [0 for i in range(53)]
    for i, line in enumerate(lines):
        for char in line:
            if char == '\n':
                continue
            existence[letterToPriority(char)] = existence[letterToPriority(char)] | (1<<i)
    for i in range(1,53):
        if existence[i] == (1<<len(lines)) - 1:
            return i
    raise Exception("There is no common letter in " + str(lines))
        

if __name__ == '__main__':
    with open('3.in','r') as fin:
        lns = fin.readlines()
    totPriority = 0
    for ln in lns:
        totPriority += letterToPriority(lineToLetter(ln))

    print(totPriority)
    
    with open('3.in','r') as fin:
        lns = fin.readlines()

    totPriority2 = 0
    for i in range(0,len(lns),3):
        lines = lns[i:i+3]
        totPriority2 += findCommonLetter_Part2(lines)

    print(totPriority2)
    
