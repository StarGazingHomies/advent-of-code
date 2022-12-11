def ints(line):
    i = 0
    rtrns = []
    while i < len(line):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0']:
            j = i + 1
            while j < len(line) and line[j] in ['1','2','3','4','5','6','7','8','9','0']:
                j += 1
            
            rtrns.append(int(line[i:j]))
            i = j
        i += 1
    return rtrns

class Monkey():
    def __init__(self, items, op, check, true, false):
        self.items = items
        self.op = op
        self.check = check
        self.true = true
        self.false = false

    def __str__(self):
        return f"Monkey<op: {op}, check: {check}, true: {true}, false: {false}, items: {items}>"

if __name__ == '__main__':
    with open("11.in","r") as fin:
        lns = fin.readlines()
    
    monkeys = []
    
    for i in range(0,len(lns),7):
        # Items, Op, Check, True, False (in that order)
        monkeys.append(Monkey(ints(lns[i+1]), lns[i+2][13:-1], ints(lns[i+3])[0], ints(lns[i+4])[0], ints(lns[i+5])[0]))

    # Want to be able to sort it
    inspectCnt = [0 for i in range(len(monkeys))]

    for i in range(10000):
        for i in range(len(monkeys)):
            curMonkey = monkeys[i]
            while len(curMonkey.items) > 0:
                inspectCnt[i]+=1
                item = curMonkey.items.pop(0)
                # Go down the VERY UNSAFE, DONT USE IN ACTUAL CODE route
                old = item
                exec(curMonkey.op)

                # Modulo for prt 2, so numbers are manageable
                new = new % 9699690

                # Throw the item accordingly
                if (new % curMonkey.check == 0):
                    monkeys[curMonkey.true].items.append(new)
                else:
                    monkeys[curMonkey.false].items.append(new)
    print(inspectCnt)
    inspectCnt.sort()
    print(inspectCnt)
    

                
