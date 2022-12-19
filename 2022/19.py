import functools
import sys
import math
import time

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

# Ugh, abstraction = pain if not done well.

##class GameState(object):
##    def __init__(self, orer, cr, obsr, gr, ore, clay, obsidian, geode):
##        self.oreRobots = orer
##        self.clayRobots = cr
##        self.obsidianRobots = obsr
##        self.geodeRobots = gr
##        self.ore = ore
##        self.clay = clay
##        self.obsidian = obsidian
##        self.geode = geode
##
##    def __str__(self):
##        return f"GameState<{self.oreRobots}, {self.clayRobots}, {self.obsidianRobots}, {self.geodeRobots}, {self.ore}, {self.clay}, {self.obsidian}, {self.geode}>"
##
##    __repr__ = __str__
##    
##    def copy(self):
##        return GameState(self.oreRobots, self.clayRobots, \
##                         self.obsidianRobots, self.geodeRobots, \
##                         self.ore, self.clay, self.obsidian, self.geode)
##
##    
##    def next(self, time=1):
##        self.ore += self.oreRobots * time
##        self.clay += self.clayRobots * time
##        self.obsidian += self.obsidianRobots * time
##        self.geode += self.geodeRobots * time
##        return self
##
##    def __lt__(self, other):
##        return (self.ore <= other.ore and \
##                self.clay <= other.clay and \
##                self.obsidian <= other.obsidian and \
##                self.geode <= other.geode and \
##                self.oreRobots <= other.oreRobots and \
##                self.clayRobots <= other.clayRobots and \
##                self.obsidianRobots <= other.obsidianRobots and \
##                self.geodeRobots <= other.geodeRobots)
##
##    def __eq__(self, other):
##        return (self.ore == other.ore and \
##                self.clay == other.clay and \
##                self.obsidian == other.obsidian and \
##                self.geode == other.geode and \
##                self.oreRobots == other.oreRobots and \
##                self.clayRobots == other.clayRobots and \
##                self.obsidianRobots == other.obsidianRobots and \
##                self.geodeRobots == other.geodeRobots)
##
##    def quality(self, bp):
##        return self.geode * 8 + \
##               (self.obsidian + bp[5]*self.geodeRobots) * 4 + \
##               (self.clay + bp[3]*self.obsidianRobots) * 2 + \
##               self.ore + bp[4]*self.geodeRobots + bp[2] * self.obsidianRobots + bp[1] * self.clayRobots + bp[0] * self.oreRobots
##
##    def craftOre(self, bps):
##        self.ore -= bps[0]
##        self.oreRobots += 1
##        return self
##        
##    def craftClay(self, bps):
##        self.ore -= bps[1]
##        self.clayRobots += 1
##        return self
##        
##    def craftObby(self, bps):
##        self.ore -= bps[2]
##        self.clay -= bps[3]
##        self.obsidianRobots += 1
##        return self
##        
##    def craftGeode(self, bps):
##        self.ore -= bps[4]
##        self.obsidian -= bps[5]
##        self.geodeRobots += 1
##        return self
##
##    def timeUntil(self, bps):
##        # ore
##        try:
##            a = max(0, math.ceil((bps[0] - self.ore)/self.oreRobots))
##        except ZeroDivisionError:
##            a = -2
##        try:
##            b = max(0, math.ceil((bps[1] - self.ore)/self.oreRobots))
##        except ZeroDivisionError:
##            b = -2
##        try:
##            c = max(0, math.ceil((bps[2] - self.ore)/self.oreRobots), \
##                    math.ceil((bps[3] - self.clay)/self.clayRobots))
##        except ZeroDivisionError:
##            c = -2
##        try:
##            d = max(0, math.ceil((bps[4] - self.ore)/self.oreRobots), \
##                     math.ceil((bps[5] - self.obsidian)/self.obsidianRobots))
##        except ZeroDivisionError:
##            d = -2
##        return a+1, b+1, c+1, d+1
##    
##    def blueprints(self, bps):
##            rtrn = []
##            if self.ore >= bps[0]:
##                # Ore
##                newGameState = GameState(self.oreRobots+1, self.clayRobots, \
##                                         self.obsidianRobots, self.geodeRobots, \
##                                         self.ore-bps[0], self.clay, self.obsidian, self.geode)
##                newGameState.next()
##                newGameState.ore -= 1
##                rtrn.append(newGameState)
##            if self.ore >= bps[1]:
##                # clay
##                newGameState = GameState(self.oreRobots, self.clayRobots+1, \
##                                         self.obsidianRobots, self.geodeRobots, \
##                                         self.ore-bps[1], self.clay, self.obsidian, self.geode)
##                newGameState.next()
##                newGameState.clay -= 1
##                rtrn.append(newGameState)
##            if self.ore >= bps[2] and self.clay >= bps[3]:
##                # obby
##                newGameState = GameState(self.oreRobots, self.clayRobots, \
##                                         self.obsidianRobots+1, self.geodeRobots, \
##                                         self.ore-bps[2], self.clay-bps[3], self.obsidian, self.geode)
##                newGameState.next()
##                newGameState.obsidian -= 1
##                rtrn.append(newGameState)
##            if self.ore >= bps[4] and self.obsidian >= bps[5]:
##                # geode
##                newGameState = GameState(self.oreRobots, self.clayRobots, \
##                                         self.obsidianRobots, self.geodeRobots+1, \
##                                         self.ore-bps[4], self.clay, self.obsidian-bps[5], self.geode)
##                newGameState.next()
##                newGameState.geode -= 1
##                rtrn.append(newGameState)
##            return rtrn

# Magic constants lol
MAX_DFS = 1500
WEIGHTS = [2,17,94,358]

def quality(state, bp):
    s = 0
    r, m = state
    n = list(m)
    for i in range(4):
        for j in range(4):
            n[i] += r[j]*bp[j][i]
        s += WEIGHTS[i] * n[i]
    return s

def bfs(blueprint, minutes):
    #print(blueprint)
    cur = [((1,0,0,0),(0,0,0,0))]
    # ugh lists are mutable and do weird stuff
    for time in range(minutes):
        new = []
        for robots, inventory in cur:
##            print(robots, inventory)
            newInventory = tuple([inventory[i]+robots[i] for i in range(4)])
            # Do nothing
            new.append((robots, newInventory))
            # Craft new robots?
            for i in range(4):
                for j in range(4):
                    if blueprint[i][j] > inventory[j]:
                        break
                else:
##                    if i == 3:
##                        print("->", i)
                    newRobots = list(robots)
                    newRobots[i]+=1
                    newRobots = tuple(newRobots)
                    newNewInventory = tuple([newInventory[r]-blueprint[i][r] for r in range(4)])
                    new.append((newRobots, newNewInventory))

##        print(time, len(new))
##        input()
            
        new.sort(key=lambda x:quality(x, blueprint), reverse=True)
        cur = new[:MAX_DFS]
    new.sort(key=lambda x:x[1][3], reverse=True)
    return new[0][1][3]

if __name__ == '__main__':
    with open('19.in','r') as fin:
        lns = fin.readlines()

    bps = []
    for ln in lns:
        tmp = ints(ln)[1:]
        bps.append(((tmp[0], 0, 0, 0), \
                    (tmp[1], 0, 0, 0), \
                    (tmp[2], tmp[3], 0, 0), \
                    (tmp[4], 0, tmp[5], 0)))
    #print(bps)
    
##    print(bps)
##    print(GameState(0,0,0,0,100,100,100,100).blueprints(bps[0]))

    pt1 = 0
    pt2 = 1
    t1 = time.perf_counter()
    for bpn, bp in enumerate(bps):
        pt1 += (bpn+1)*bfs(bp,24)
        if bpn < 3:
            res = bfs(bp, 32)
            pt2 *= res
            print(res)
            # 10 37 32

##        states = [[] for i in range(25)]
##        states[0].append(GameState(1,0,0,0,0,0,0,0))
##
##        obbyUnlock = 100
##        geodeUnlock = 100
##
##        for i in range(0,24):
##
##            states[i].sort()
##            states[i] = states[i][:30000]
##            if len(states[i]) < 3000:
##                for m in range(len(states[i])-1, -1, -1):
##                    for n in range(m,len(states[i])):
##                        if (m==n):
##                            continue
##
##                        if states[i][m] < states[i][n]:
##                            states[i].pop(m)
##                            break
####                        s1 = states[i][m].copy().next(24-i)
####                        s2 = states[i][n].copy().next(24-i)
####                        if s1.geode < s2.geode and s1.obsidian < s2.obsidian and s1.clay < s2.clay and s1.ore < s2.ore:
####                            states[i].pop(m)
####                            break
##
####            print(i, len(states[i]))
####            print(states[i])
####            input()
##            
##            for gs in states[i]:
##                #print(gs)
####                for gsn in gs.blueprints(bp):
####                    states[i+1].append(gsn)
####                states[i+1].append(gs.next())
##                a, b, c, d = gs.timeUntil(bp)
####                print(gs)
####                print(a,b,c,d)
##                if (gs.obsidianRobots == 0 and i+c>obbyUnlock+2):
##                    continue
##                if (gs.geodeRobots == 0 and i+d>geodeUnlock):
##                    continue
##                if a != -1 and i+a < 25:
##                    ngs = gs.copy().next(a).craftOre(bp)
##                    states[i+a].append(ngs)
##                if b != -1 and i+b < 25:
##                    ngs = gs.copy().next(b).craftClay(bp)
##                    states[i+b].append(ngs)
##                if c != -1 and i+c < 25:
##                    ngs = gs.copy().next(c).craftObby(bp)
##                    states[i+c].append(ngs)
##                    obbyUnlock = min(i+c, obbyUnlock)
####                    print("!", obbyUnlock, gs)
##                if d != -1 and i+d < 25:
##                    ngs = gs.copy().next(d).craftGeode(bp)
##                    states[i+d].append(ngs)
##                    geodeUnlock = min(i+d, geodeUnlock)
####                    print("!!", geodeUnlock, gs)
##
##        allEndStates = []
##        for i in range(0,24):
##            for gs in states[i]:
##                allEndStates.append(gs.next(24-i))
##        allEndStates.sort(key=lambda x:-x.geode)
##        print(bpn, allEndStates[0])
##        r += (bpn+1) * allEndStates[0].geode
    print(pt1, pt2)
    t2 = time.perf_counter()
    print("Time taken:", t2-t1)
