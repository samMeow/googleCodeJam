import sys
from decimal import Decimal

# N < 30
# K < 10^9
def solution(K, brought):
    own = sorted(set(brought))
    if len(own) == K:
        return float(0)

    N = len(own)
    gaps = [0] * (N-1)
    for i in range(N - 1):
        gaps[i] = own[i+1] - own[i]
    before = own[0] - 1
    after = K - own[-1]
    points = [before, *[ int(x/2) for x in gaps], after]
    points = sorted(points)

    p2 = [x - 1 for x in gaps] + [0]
    high = max(points[-1] + points[-2], max(p2))

    return Decimal(high) / K

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line1 = sys.stdin.readline()
    [_, K] = [ int(x) for x in line1.split(' ') ]
    line2 = sys.stdin.readline().rstrip('\n')
    ques = [ int(x) for x in line2.split(' ') ]
    print("Case #{}: {}".format(i+1, solution(K, ques)))
