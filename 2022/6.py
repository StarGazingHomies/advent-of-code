if __name__ == '__main__':
    lastLetters = [0 for i in range(26)]
    with open('6.in','r') as fin:
        lns = fin.readlines()

    # Part 1
    for index in range(0,len(lns[0])):
        lastLetters[ord(lns[0][index])-ord('a')] += 1
        if (index >= 4):
            lastLetters[ord(lns[0][index-4])-ord('a')] -= 1
        if (index >= 3):
            satisfy = True
            for i in range(26):
                if (lastLetters[i]) > 1:
                    satisfy = False
            if satisfy:
                print(index + 1)
                break
        #print(lastLetters)

    lastLetters = [0 for i in range(26)]
    # Part 2
    for index in range(0,len(lns[0])):
        lastLetters[ord(lns[0][index])-ord('a')] += 1
        if (index >= 14):
            lastLetters[ord(lns[0][index-14])-ord('a')] -= 1
        if (index >= 13):
            satisfy = True
            for i in range(26):
                if (lastLetters[i]) > 1:
                    satisfy = False
            if satisfy:
                print(index + 1)
                break
        #print(lastLetters)
        
