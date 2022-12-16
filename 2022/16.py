import functools
import sys

def ints(line):
    i = 0
    rtrns = []
    while i < len(line):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0', '-']:
            j = i + 1
            while j < len(line) and line[j] in ['1','2','3','4','5','6','7','8','9','0', '-']:
                j += 1
            
            rtrns.append(int(line[i:j]))
            i = j
        i += 1
    return rtrns


def nameToNum(name):
    return (ord(name[0])-ord('A'))*26+ord(name[1])-ord('A')

def getCapitals(ln):
    rtrn = ''
    for i in ln:
        if ord('A') <= ord(i) <= ord('Z'):
            rtrn += i
    return rtrn

@functools.cache
def bfs(start, end):
    global graph
    pos = [start]
    vis = [False for _ in range(len(graph))]
    cnt = 0
    
    while len(pos) > 0:
        newPos = []
        for x in pos:
            if vis[x]:
                continue
            vis[x] = True

            if x == end:
                return cnt
            
            # If you can go somewhere
            for y in graph[x]:
                newPos.append(y)

        pos = newPos
        cnt += 1
    # Something prolly went wrong
    return -1

def getValves(grid, flow, pos, steps):
    maxR = 0
    for v in range(len(grid[pos])):
        if flow[v] == 0:
            continue
        
        dist = grid[pos][v]
        
        if steps < dist + 1:
            continue
        
        flowCopy = flow.copy()
        flowCopy[v] = 0
        thisResult = getValves(grid, flowCopy, v, steps-dist-1)
        thisResult += (steps - dist - 1) * flow[v]
        maxR = max(thisResult, maxR)

    return maxR

def getValves2(grid, flow, pos1, pos2, steps1, steps2):
    maxR = 0
    if steps1 < steps2:
        for v in range(len(grid[pos2])):
            if flow[v] == 0:
                continue
            
            dist = grid[pos2][v]
            
            if steps2 < dist + 1:
                continue
            
            flowCopy = flow.copy()
            flowCopy[v] = 0
            thisResult = getValves2(grid, flowCopy, pos1, v, steps1, steps2-dist-1)
            thisResult += (steps2 - dist - 1) * flow[v]
            maxR = max(thisResult, maxR)
    else:
        for v in range(len(grid[pos1])):
            if flow[v] == 0:
                continue
            
            dist = grid[pos1][v]
            
            if steps1 < dist + 1:
                continue
            
            flowCopy = flow.copy()
            flowCopy[v] = 0
            thisResult = getValves2(grid, flowCopy, v, pos2, steps1-dist-1, steps2)
            thisResult += (steps1 - dist - 1) * flow[v]
            maxR = max(thisResult, maxR)

    return maxR
     

if __name__ == '__main__':
    with open('16.in','r') as fin:
        lns = fin.readlines()

    graph = [[] for i in range(1000)]
    flow = [0 for i in range(1000)]
    # Construct graph
    for ln in lns:
        v = ln[6:8]
        fr = ints(ln)[0]
        i = nameToNum(v)
        flow[i] = fr
        lead_to = getCapitals(ln.split(';')[1])
        for j in range(0,len(lead_to),2):
            graph[i].append(nameToNum(lead_to[j:j+2]))
        valid_pos.append(i)
        
    # Part 1
    simpVerts = []
    newFlow = []
    simpVerts.append(0)
    newFlow.append(flow[0])
    for i, f in enumerate(flow):
        if f != 0:
            simpVerts.append(i)
            newFlow.append(f)

    newGraph = [[0 for _ in range(len(simpVerts))] for _ in range(len(simpVerts))]
    for i, x in enumerate(simpVerts):
        for j, y in enumerate(simpVerts):
            dist = bfs(x,y)
            newGraph[i][j] = dist

    print(getValves(newGraph, newFlow, 0, 30))
    print(getValves2(newGraph, newFlow, 0, 0, 26, 26))
    sys.exit()
    # Part 2 - 
    simpVerts.pop(0)
    newFlow.pop(0)
    print(dp(graph, flow))
