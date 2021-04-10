import sys

def solution(ques):
    temp = [ (v,i) for i, v in enumerate(ques)]
    temp = sorted(temp)
    temp = [ v[1] for v in temp ]
    accu = 0
    for i in range(len(temp)):
        v = temp[i]
        accu += v - i + 1
        temp[i] = i
        for j in range(i+1, len(ques)):
            if temp[j] < v:
                temp[j] = v + i - temp[j]
    return accu - 1



testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline().rstrip('\n')
    ques = [ int(x) for x in line2.split(' ') ]
    print("Case #{}: {}".format(i+1, solution(ques)))
