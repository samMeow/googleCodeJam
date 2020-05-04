import sys

def minConcat(str1, str2):
    # startpt = min(len(str1) - len(str2), 0)
    # for i in range(startpt, len(str1)):
    #     if str2.startswith(str1[i:]):
    #         return str1[0:i] + str2
    return str1 + str2


def solution(strs):
    pattern = [ line.split('*') for line in strs ]

    pattern.sort(key = lambda x: x[-1][::-1])
    end = ''
    for p in pattern:
        if p[-1] != '':
            if p[-1].endswith(end):
                end = p[-1]
            else:
                return '*'
    pattern.sort(key = lambda x: x[0])
    head = ''
    for p in pattern:
        if p[0] != '':
            if p[0].startswith(head):
                head = p[0]
            else:
                return '*'

    temp = [ p[1:-1] for p in pattern if len(p[1:-1]) > 0 ]
    stack = temp
    while len(stack) > 0:
        p = stack.pop(0)
        if len(p) > 0:
            head = minConcat(head, p[0])
            stack.append(p[1:])
    
    result = minConcat(head, end)
    return result

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    line = sys.stdin.readline()
    buffer = []
    for _ in range(int(line)):
        buffer.append(sys.stdin.readline().rstrip('\n'))
    print("Case #{}: {}".format(i+1, solution(buffer)))