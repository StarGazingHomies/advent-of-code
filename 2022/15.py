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

class SegTree(object):
    def __init__(self, init_val, debug = False):
        self.debugPrints = debug
        self.n = len(init_val)
        self.val = [0 for _ in range(self.n<<2)]
        self.lazy = [0 for _ in range(self.n<<2)]
        self.build(init_val)

    def push_up(self, rt):
        self.val[rt] = self.val[rt*2] + self.val[rt*2+1]

    def push_down(self, rt, l, r):
        if self.lazy[rt] != 0:
            mid = (l+r)//2
            self.lazy[rt*2]   += 1
            self.lazy[rt*2+1] += 1
            self.val[rt*2]    += mid - l + 1
            self.val[rt*2+1]  += r - mid
            self.lazy[rt] = 0

    def build(self, init_val, rt=1, l=0, r=-1):
        if r == -1:
            r = self.n-1
        if self.debugPrints:
            print(f"Building segtree at {rt} for range {l} to {r}.")
        
        if l==r:
            self.val[rt] = init_val[l]
        else:
            mid = (l+r)//2
            self.build(init_val, rt*2,   l,     mid)
            self.build(init_val, rt*2+1, mid+1, r  )
            self.push_up(rt)

    def update_single(self, idx, add, rt=1, l=0, r=-1):
        if r == -1:
            r = self.n-1
        
        if l==r:
            self.val[rt] += add
            return
        mid = (l+r)//2
        if (idx <= mid):
            self.update_single(idx, add, rt*2, l, mid)
        else:
            self.update_single(idx, add, rt*2+1, mid+1, r)
        self.push_up(rt)

    def query(self, ql, qr, rt=1, l=0, r=-1):
        if r == -1:
            r = self.n-1
        
        if ql > r or qr < l:
            return 0
        if ql <= l and qr >= r:
            if self.debugPrints:
                print(f"Accessed values at {rt} for range {l} to {r}.")
            return self.val[rt]
        
        self.push_down(rt, l, r)
        mid = (l+r)//2
        return self.query(ql, qr, rt*2, l, mid) + self.query(ql, qr, rt*2+1, mid+1, r)

    def update_region(self, ul, ur, rt=1, l=0, r=-1):
        if (r == -1):
            r = self.n - 1
        
        if (ul>r or ur<l):
            return
        if (ul <= l and ur >= r):
            if self.debugPrints:
                print(f"Updated region at {rt} for range {l} to {r}.")
            self.val[rt] += (r - l + 1)
            self.lazy[rt] = 1
            return

        self.push_down(rt)
        mid = (l+r)//2
        self.update_region(ul, ur, rt*2, l, mid)
        self.update_region(ul, ur, rt*2+1, mid+1, r)
        self.push_up(rt)

    def debug(self, rt=1, l=0, r=-1, d=0):
        if r == -1:
            r = self.n - 1
        if self.debugPrints:
            print(f"{'  '*d}{rt}: [{l}, {r}]; val: {self.val[rt]}, lazy: {self.lazy[rt]}")
        if (l==r):
            return
        mid = (l+r)//2
        self.debug(rt*2, l, mid, d+1)
        self.debug(rt*2+1, mid+1, r, d+1)

if __name__ == '__main__':
    with open('15.in','r') as fin:
        lns = fin.readlines()

    l = []
    for ln in lns:
        l.append(ints(ln))

##    for target in range(0,20):
##    #if True:
##        a = [0 for i in range(100000)]
##
##        cnt = 0
##        offset = 50000
##        #target = 8
##        displayHalfW = 30
##        for xs, ys, xb, yb in l:
##            xs = xs + offset
##            xb = xb + offset
##            dst = abs(xs-xb)+abs(ys-yb)
##            dst2m =  dst - abs(ys-target)
##            if dst2m >= 0:
##                a[xs - dst2m] += 1
##                a[xs + dst2m + 1] += -1
##            #print(xs, ys, xb, yb, xs, dst2m, xs - dst2m, xs + dst2m + 1)
##
##        k = 0
##        for i in range(len(a)):
##            k += a[i]
##            if (k > 0):
##                for xs, ys, xb, yb in l:
##                    if xs + offset == i and xb == target:
##                        if offset - displayHalfW < i < offset + displayHalfW:
##                            print(end='S')
##                        break
##                    
##                    if yb == target and xb + offset == i:
##                        if offset - displayHalfW < i < offset + displayHalfW:
##                            print(end='B')
##                        break
##                else:
##                    if offset - displayHalfW < i < offset + displayHalfW:
##                        print(end=str(k))
##                    cnt += 1
##            else:
##                if offset - displayHalfW < i < offset + displayHalfW:
##                    if k < 0:
##                        print(end='!')
##                    else:
##                        print(end='.')
##        print()
##

    # Part 1
##    a = [0 for i in range(10000000)]
##
##    cnt = 0
##    offset = 5000000
##    target = 2000000
##    displayHalfW = 0
##    print("xs",'ys','xb','yb','dst','u','v',sep='\t')
##    for xs, ys, xb, yb in l:
##        xs = xs + offset
##        xb = xb + offset
##        dst = abs(xs-xb)+abs(ys-yb)
##        dst2m =  dst - abs(ys-target)
##        if dst2m >= 0:
##            a[xs - dst2m] += 1
##            a[xs + dst2m + 1] += -1
##        print(xs-offset, ys, xb-offset, yb, xs, dst2m, xs - dst2m-offset, xs + dst2m + 1-offset, sep='\t')
##
##    k = 0
##    for i in range(len(a)):
##        k += a[i]
##        if (k > 0):
##            for xs, ys, xb, yb in l:
##                if xs + offset == i and xb == target:
##                    if offset - displayHalfW < i < offset + displayHalfW:
##                        print(end='S')
##                    break
##                
##                if yb == target and xb + offset == i:
##                    if offset - displayHalfW < i < offset + displayHalfW:
##                        print(end='B')
##                    break
##            else:
##                if offset - displayHalfW < i < offset + displayHalfW:
##                    print(end=str(k))
##                cnt += 1
##        else:
##            if offset - displayHalfW < i < offset + displayHalfW:
##                if k < 0:
##                    print(end='!')
##                else:
##                    print(end='.')
##    print()
##    print(cnt)
    
    #print("xs",'ys','xb','yb','dst','u','v',sep='\t')

    for y in range(0,4000001):
        
        ops = []
        for xs, ys, xb, yb in l:
            dst = abs(xs-xb)+abs(ys-yb)
            dst2y =  dst - abs(ys-y)
            if dst2y >= 0:
                ops.append((xs - dst2y, 1))
                ops.append((xs + dst2y + 1, -1))
        ops.sort(key=lambda x:x[0])

        n = 0
        for x, o in ops:
            n += o
            if n==0 and 0 <= x <= 4000000:
                print(x,y)


