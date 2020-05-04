import sys

def solution(x, y, m):
    pos = (x, y)
    step = 0
    for move in m:
        if move == 'E':
            pos = (pos[0] + 1, pos[1])
        elif move == 'S':
            pos = (pos[0], pos[1] -1)
        elif move == 'W':
            pos = (pos[0] - 1, pos[1])
        elif move == 'N':
            pos = (pos[0], pos[1] + 1)

        step = step + 1
        if abs(pos[0]) + abs(pos[1]) <= step:
            return step

    return 'IMPOSSIBLE'

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    [x, y, m] = sys.stdin.readline().rstrip('\n').split()
    print("Case #{}: {}".format(i+1, solution(
        int(x),
        int(y),
        m
    )))