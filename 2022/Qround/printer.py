import sys

def solution(input):
    buffer = []
    for i in range(4):
        mini = min([ x[i] for x in input ])
        buffer.append(mini)
    if sum(buffer) < 1000000:
        return 'IMPOSSIBLE'
    k = 1000000
    temp = []
    for v in buffer:
        if  v >= k:
            temp.append(str(k))
            k = 0
        else:
            temp.append(str(v))
            k -= v
    return ' '.join(temp)

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    buffer = []
    for _ in range(3):
        line = sys.stdin.readline().rstrip('\n')
        buffer.append([ int(x) for x in line.split(' ') ])
    ans = solution(buffer)
    print("Case #{}: {}".format(i+1, ans))
