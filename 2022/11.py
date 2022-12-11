

if __name__ == '__main__':
    with open("11.in","r") as fin:
        lns = fin.readlines()

    monkeyItems = []
    monkeyCondition = []
    monkeyOp = []
    monkeyCheck = []
    monkeyTrueOp = []
    monkeyFalseOp = []
    for i in range(0,len(lns),7):
        monkeyIndex = int(lns[i][7:-2])
        monkeyItems.append(eval("["+lns[i+1][17:]+"]"))
        monkeyOp.append(lns[i+2][13:][:-1]) # Use exec(operation)
        monkeyCheck.append(int(lns[i+3][21:]))
        monkeyTrueOp.append(int(lns[i+4][29:-1]))
        monkeyFalseOp.append(int(lns[i+5][30:-1]))
        # print(monkeyIndex, monkeyList, operation, check)
    print(monkeyTrueOp, monkeyFalseOp)

    inspectCnt = [0 for i in range(len(monkeyItems))]

    for i in range(10000):
##        print(f"Round {i+1}")
        newMonkeyItems = [[] for _ in range(len(monkeyItems))]
        for i in range(len(monkeyItems)):
##            print(f"Monkey {i}:")
##            print(f"MonkeyItems {monkeyItems[i]}")
            while len(monkeyItems[i]) > 0:
                inspectCnt[i]+=1
                item = monkeyItems[i].pop(0)
##                print("Old:",item)
                old = item
                exec(monkeyOp[i])
                new = new % 9699690
##                print("New:",new)
                if (new % monkeyCheck[i] == 0):
##                    print("Thrown to", monkeyTrueOp[i])
                    monkeyItems[monkeyTrueOp[i]].append(new)
                else:
##                    print("Thrown to", monkeyFalseOp[i])
                    monkeyItems[monkeyFalseOp[i]].append(new)
##            print(monkeyItems)
##            print("----------------")
    print(inspectCnt)
    inspectCnt.sort()
    print(inspectCnt)
    

                
