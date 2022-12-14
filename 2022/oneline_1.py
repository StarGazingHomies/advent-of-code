# This is a one-line program for day 1 :)
# Part 1
print(sorted(eval('['+''.join([ln.replace('\n','+') if ln != '\n' else '0,' for ln in open('1.in','r').readlines()])+']'))[-1])

# Part 2
print(sum(sorted(eval('['+''.join([ln.replace('\n','+') if ln != '\n' else '0,' for ln in open('1.in','r').readlines()])+']'))[-1:-4:-1]))

