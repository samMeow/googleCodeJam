import sys

def solution(input):
    k = 1
    for v in sorted(input):
        if v >= k:
            k += 1
    return k - 1

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    sys.stdin.readline()
    line1 = sys.stdin.readline().rstrip('\n')
    line2 = sys.stdin.readline().rstrip('\n')
    ans = solution(
        [ int(x) for x in line1.split(' ') ],
        [ int(x) for x in line2.split(' ') ],
    )
    print("Case #{}: {}".format(i+1, ans))
