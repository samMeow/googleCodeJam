import sys

def solution(input):
    newStr = ''
    for i, v in enumerate(input):
        newStr = newStr + v
        combine = input[:i]+v+input[i:]
        if combine < input:
            newStr = newStr + v
    return newStr

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line = sys.stdin.readline().rstrip('\n')
    ans = solution(line)
    print("Case #{}: {}".format(i+1, ans))
