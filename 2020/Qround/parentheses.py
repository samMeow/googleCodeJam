import sys

def solution(line):
    buffer = []
    lastPar = 0
    for i in line:
        if int(i) > lastPar:
            for _ in range(int(i) - lastPar):
                buffer.append('(')
            lastPar = int(i)
            buffer.append(i)
        elif int(i) < lastPar:
            for _ in range(lastPar - int(i)):
                buffer.append(')')
            lastPar = int(i)
            buffer.append(i)
        else:
            buffer.append(i)
    for _ in range(lastPar):
        buffer.append(')')
    return ''.join(buffer)

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line = sys.stdin.readline().rstrip('\n')
    print("Case #{}: {}".format(i+1, solution(line)))