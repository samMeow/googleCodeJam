import sys

def solution(acts):
    c = [ True for _ in range(0, 1440) ]
    j = [ True for _ in range(0, 1440) ]
    
    sch = [ '' for _ in range(len(acts)) ]
    
    sortacts = [ (x[0], x[1], i) for i, x in enumerate(acts) ]
    sortacts.sort(key = lambda x: (x[0], x[1]))
    for a in sortacts:
        if all(c[a[0]:a[1]]):
            c[a[0]:a[1]] = [ False for _ in c[a[0]:a[1]] ]
            sch[a[2]] = 'C'
        elif all(j[a[0]:a[1]]):
            j[a[0]:a[1]] = [ False for _ in j[a[0]:a[1]] ]
            sch[a[2]] = 'J'
        else:
            return 'IMPOSSIBLE'
    return ''.join(sch)



testcase = sys.stdin.readline()
for i in range(int(testcase)):
    n = sys.stdin.readline()
    buffer = []
    for _ in range(int(n)):
        line = sys.stdin.readline().rstrip('\n')
        buffer.append([ int(x) for x in line.split(' ') ])
    print("Case #{}: {}".format(i+1, solution(buffer)))
