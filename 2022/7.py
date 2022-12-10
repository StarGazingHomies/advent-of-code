
MAX_FILE_AND_FOLDER_CNT = 20000
dirSizes = [0 for i in range(MAX_FILE_AND_FOLDER_CNT)]

def debugTraverse(dirNames, itemType, children, parent, pos=0, depth=0):
    global dirSizes
    print("  "*depth + "- " + dirNames[pos], end = ' ')
    if (itemType[pos] == -1):
        print(f"(dir, size =", dirSizes[pos], end = ')\n')
        for i in children[pos]:
            debugTraverse(dirNames, itemType, children, parent, i, depth+1)
    else:
        print(f"(file, size =", itemType[pos], end = ')\n')



def findDirSize(dirNames, itemType, children, parent, pos=0, depth=0):
    #global sizesLessThan100k
    if (itemType[pos] == -1):
        totSize = 0
        for i in children[pos]:
            totSize += findDirSize(dirNames, itemType, children, parent, i, depth+1)
        
        #if (totSize <= 100000):
        #    sizesLessThan100k.append(totSize)

        dirSizes[pos] = totSize
        # Bruh i forgot how to use fstrings
        return totSize
    else:
        return itemType[pos]


if __name__ == '__main__':
    wp = 1
    dirNames = ['/' for i in range(MAX_FILE_AND_FOLDER_CNT)]
    itemType = [-1 for i in range(MAX_FILE_AND_FOLDER_CNT)]
    children = [[] for i in range(MAX_FILE_AND_FOLDER_CNT)]
    parent = [-1 for i in range(MAX_FILE_AND_FOLDER_CNT)]
    # 0 is root
    curPos = 0

    with open('7.in','r') as fin:
        lns = fin.readlines()

    for ln in lns:
        #print("-------------------")
        # Do stuff
        #print(ln)
        if ln[0] == '$':
            # cd
            if ln[2:4] == 'cd':
                pathToGo = ln[5:-1]
                if pathToGo == '/':
                    curPos = 0
                elif pathToGo == '..':
                    curPos = parent[curPos]
                else:
                    for c in children[curPos]:
                        if dirNames[c] == pathToGo:
                            curPos = c
                            break
                    else:
                        print("Something went horribly wrong, this dir doesn't exist!")
            #Ignore ls's, the input guarantees no $ means it's a file in the current directory?
        else:
            fileType, fileName = ln.split(' ')
            if fileType == 'dir':
                fileType = -1
            else:
                fileType = int(fileType)
            children[curPos].append(wp)
            parent[wp] = curPos
            itemType[wp] = fileType
            dirNames[wp] = fileName[:-1] # Remove \n
            wp += 1
            #print(dirNames, children, parent, itemType, sep='\n')
            
    # Aaand file structure is done... need to check repeat?
    findDirSize(dirNames, itemType, children, parent)
    # debugTraverse(dirNames, itemType, children, parent)

    totValidSize = 0
    for d in range(MAX_FILE_AND_FOLDER_CNT):
        if (dirSizes[d] < 100000):
            totValidSize += dirSizes[d]
    print(totValidSize)

    # Part 2 is much easier now that part 1 is done
    totalDiskSpace = 70000000
    requiredSpace = 30000000
    usedSpace = dirSizes[0]
    # Deletion req
    requiredSpace -= (totalDiskSpace - usedSpace)

    smolestSatisfactory = 1e100
    for d in range(MAX_FILE_AND_FOLDER_CNT):
        if (requiredSpace < dirSizes[d] < smolestSatisfactory):
            smolestSatisfactory = dirSizes[d]
    print(smolestSatisfactory)
