import sys

def isUniq(ar):
    return len(set(ar)) == len(ar)

def colCount(ma):
    count = 0
    for i in range(len(ma)):
        if not isUniq([ x[i] for x in ma]):
            count = count + 1
    return count

def rowCount(ma):
    count = 0
    for line in ma:
        if not isUniq(line):
            count = count + 1
    return count

def dia(ma):
    sum = 0
    for i in range(len(ma)):
        sum = sum + int(ma[i][i])
    return sum

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    n = sys.stdin.readline()
    buffer = []
    for line in range(int(n)):
        l = sys.stdin.readline();
        buffer.append(l.rstrip('\n').split(' '))
    print("Case #{}: {} {} {}".format(
        i + 1,
        dia(buffer),
        rowCount(buffer),
        colCount(buffer),
    ))