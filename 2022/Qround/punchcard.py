import sys

def solution(input):
    [r, c] = input
    buffer = []
    for i in range(2 * r + 1):
        temp = []
        for j in range(2 * c + 1):
            x = '.'
            if i % 2 == 0 and j % 2 == 0:
                x = '+'
            elif i % 2 == 0:
                x = '-'
            elif j % 2 == 0:
                x = '|'
            temp.append(x)
        buffer.append(temp)
    buffer[0][0] = '.'
    buffer[0][1] = '.'
    buffer[1][0] = '.'
    return '\n'.join([ ''.join(x) for x in buffer ])



testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line = sys.stdin.readline().rstrip('\n')
    ans = solution([ int(x) for x in line.split(' ') ])
    print("Case #{}:".format(i+1))
    print(ans)
