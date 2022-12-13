import functools

def compare(l1, l2):
    if type(l1) == int and type(l2) == int:
        if l1 < l2:
            return 1
        elif l1 == l2:
            return 0
        else:
            return -1

    if type(l1) == list and type(l2) == list:
        for i in range(min(len(l1), len(l2))):
            if compare(l1[i], l2[i]) != 0:
                return compare(l1[i], l2[i])
        if len(l1) > len(l2):
            return -1
        elif len(l1) < len(l2):
            return 1
        else:
            return 0

    if type(l1) != list:
        l1 = [l1]
    if type(l2) != list:
        l2 = [l2]
    return compare(l1, l2)

                
            
if __name__ == '__main__':
    with open('13.in','r') as fin:
        lns = fin.readlines()
    
    cnt = 0
    for i in range(0,len(lns), 3):
        a = eval(lns[i])
        b = eval(lns[i+1])
        if (compare(a,b) == 1):
            cnt += i//3 + 1
    print(cnt)

    tmp = []
    for i in range(len(lns)):
        try:
            tmp.append(eval(lns[i]))
        except SyntaxError:
            pass
        
    key = functools.cmp_to_key(compare)
    tmp.sort(key=key)
    print(tmp.index([[2]])*tmp.index([[6]]))
