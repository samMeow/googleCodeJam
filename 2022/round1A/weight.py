import sys

def find_common(weights):
    W = len(weights[0])
    common = [ 0 ] * W
    for c in range(W):
        common[c] = min([ x[c] for x in weights ])
    return common

def solution(E, W, weights):
    accu = 0
    common = find_common(weights)
    
    return accu


testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line = sys.stdin.readline().rstrip('\n')
    [E, W] = [int(x) for x in line.split(' ')]
    buffer = []
    for _ in range(E):
        temp_line = sys.stdin.readline().rstrip('\n')
        buffer.append(
            [int(x) for x in temp_line.split(' ')]
        )
    ans = solution(E, W, buffer)
    print("Case #{}: {}".format(i+1, ans))
